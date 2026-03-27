import csv
import os
from validations import validate_name, validate_price, validate_quantity

HEADER = ["nombre", "precio", "cantidad"]


# ─────────────────────────────────────────────
#  TASK 4 – Guardar CSV
# ─────────────────────────────────────────────

def guardar_csv(inventario: list[dict], ruta: str, incluir_header: bool = True) -> None:
    """Guarda el inventario en un archivo CSV con separador coma."""

    if not inventario:
        print(" ⚠  El inventario está vacío. No hay nada que guardar.\n")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if incluir_header:
                writer.writerow(HEADER)

            for product in inventario:
                writer.writerow([
                    product["name"],
                    product["price"],
                    product["quantity"],
                ])

        print(f" ✔  Inventario guardado en: {ruta}\n")

    except PermissionError:
        print(f" ✘  Sin permisos para escribir en '{ruta}'. "
              "Verifica la ruta o los permisos del archivo.\n")
    except OSError as e:
        print(f" ✘  Error al guardar el archivo: {e}\n")


# ─────────────────────────────────────────────
#  TASK 5 – Cargar CSV
# ─────────────────────────────────────────────

def cargar_csv(ruta: str) -> list[dict] | None:
    """
    Lee un CSV y devuelve una lista de productos.
    Retorna None si el archivo no puede abrirse o el encabezado es inválido.
    Las filas con errores se omiten y se acumula un contador.
    """

    productos = []
    filas_invalidas = 0

    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            # ── Validar encabezado ──────────────────────────────
            try:
                encabezado = next(reader)
            except StopIteration:
                print(" ✘  El archivo está vacío.\n")
                return None

            encabezado_normalizado = [col.strip().lower() for col in encabezado]
            if encabezado_normalizado != HEADER:
                print(
                    f" ✘  Encabezado inválido: {encabezado_normalizado}\n"
                    f"    Se esperaba: {HEADER}\n"
                )
                return None

            # ── Leer filas ──────────────────────────────────────
            for num, fila in enumerate(reader, start=2):  # start=2 (fila 1 = header)

                # 1. Exactamente 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio_raw, cantidad_raw = (col.strip() for col in fila)

                # 2. Validar nombre
                if not validate_name(nombre):
                    filas_invalidas += 1
                    continue

                # 3. Validar precio
                if not validate_price(precio_raw):
                    filas_invalidas += 1
                    continue
                precio = float(precio_raw)

                # 4. Validar cantidad
                if not validate_quantity(cantidad_raw):
                    filas_invalidas += 1
                    continue
                cantidad = int(cantidad_raw)

                productos.append({
                    "name": nombre,
                    "price": precio,
                    "quantity": cantidad,
                })

    except FileNotFoundError:
        print(f" ✘  Archivo no encontrado: '{ruta}'\n")
        return None
    except UnicodeDecodeError:
        print(f" ✘  El archivo '{ruta}' tiene una codificación incompatible. "
              "Guárdalo como UTF-8 e intenta de nuevo.\n")
        return None
    except ValueError as e:
        print(f" ✘  Error de valor inesperado al leer el CSV: {e}\n")
        return None
    except Exception as e:
        print(f" ✘  Error inesperado al leer '{ruta}': {e}\n")
        return None

    if filas_invalidas:
        print(f" ⚠  {filas_invalidas} fila(s) inválida(s) omitida(s).")

    return productos


def _fusionar(inventario: list[dict], nuevos: list[dict]) -> tuple[list[dict], int]:
    """
    Política de fusión:
      - Si el nombre ya existe → suma la cantidad y actualiza el precio al nuevo.
      - Si no existe → agrega el producto.
    Devuelve (inventario_fusionado, cantidad_actualizados).
    """
    actualizados = 0
    inventario_copia = [p.copy() for p in inventario]

    for nuevo in nuevos:
        nombre_lower = nuevo["name"].lower()
        existente = next(
            (p for p in inventario_copia if p["name"].lower() == nombre_lower),
            None,
        )
        if existente:
            existente["quantity"] += nuevo["quantity"]
            existente["price"] = nuevo["price"]
            actualizados += 1
        else:
            inventario_copia.append(nuevo)

    return inventario_copia, actualizados


def gestionar_carga_csv(inventario: list[dict], ruta: str) -> list[dict]:
    """
    Orquesta la carga del CSV y la decisión de sobrescribir/fusionar.
    Devuelve el inventario resultante (modificado o no).
    """

    nuevos = cargar_csv(ruta)

    if nuevos is None:
        return inventario  # Hubo un error irrecuperable; no cambiar nada

    if not nuevos:
        print("  El archivo no contiene productos válidos.\n")
        return inventario

    # ── Preguntar al usuario ────────────────────────────────────
    print(f"\n Se encontraron {len(nuevos)} producto(s) válido(s) en '{ruta}'.")
    print(
        "\n Política de fusión (opción N):\n"
        "   • Si el nombre ya existe → se suma la cantidad y se actualiza el precio.\n"
        "   • Si el nombre es nuevo  → se agrega al inventario.\n"
    )

    while True:
        respuesta = input(" ¿Sobrescribir inventario actual? (S/N): ").strip().upper()
        if respuesta in ("S", "N"):
            break
        print(" Por favor ingresa S o N.")

    # ── Aplicar decisión ───────────────────────────────────────
    filas_invalidas_count = 0  # ya informadas dentro de cargar_csv

    if respuesta == "S":
        inventario_resultado = nuevos
        accion = "Reemplazo completo"
        actualizados = 0
    else:
        inventario_resultado, actualizados = _fusionar(inventario, nuevos)
        accion = "Fusión"

    # ── Resumen ────────────────────────────────────────────────
    print("\n" + "─" * 50)
    print(f"  Acción           : {accion}")
    print(f"  Productos cargados: {len(nuevos)}")
    if respuesta == "N":
        print(f"  Productos actualizados (fusión): {actualizados}")
    print(f"  Total en inventario: {len(inventario_resultado)}")
    print("─" * 50 + "\n")

    return inventario_resultado