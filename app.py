from services import search_product, calculate_statistics
from CRUD import add_product, update_product, delete_product
from CSV import guardar_csv, gestionar_carga_csv

DEFAULT_CSV_PATH = "inventario.csv"

inventory = []  # lista principal del inventario


def show_menu(inventory: list[dict]) -> None:
    print("\n" + "═" * 60)
    print(" INVENTORY LIST MANAGEMENT - MAIN MENU")
    print("═" * 60)
    print(" 1 → Add product")
    print(" 2 → Show inventory")
    print(" 3 → Search product")
    print(" 4 → Update product")
    print(" 5 → Delete product")
    print(" 6 → Calculate statistics")
    print(" 7 → Save CSV")
    print(" 8 → Upload CSV")
    print(" 9 → Go out")
    print("═" * 60)


# ── Programa principal ──────────────────────────────────────────
print("╔══════════════════════════════════════╗")
print("║     WELCOME TO THE INVENTORY         ║")
print("╚══════════════════════════════════════╝\n")

while True:
    show_menu(inventory)

    try:
        option = int(input(" → Your choice: "))
        print()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
        break                          # ← corregido: break en vez de continue
    except ValueError:
        print(" Error! You must enter a number (1-9).\n")
        continue
    except EOFError:
        print("\n\nProgram interrupted by user. Exiting...")
        break                          # ← corregido: break en vez de continue

    if option == 1:
        print(" → Adding product...")
        product_info = add_product()
        inventory.append(product_info)

    elif option == 2:
        if not inventory:
            print(" The inventory is empty.\n")
        else:
            print(" → Showing inventory...")
            for product in inventory:
                print(
                    f"   - {product['name']}: "
                    f"${product['price']:.2f} "
                    f"(quantity: {product['quantity']})"
                )

    elif option == 3:
        print(" Looking for product...")
        search_product(inventory)

    elif option == 4:
        print(" Updating product...")
        update_product(inventory)

    elif option == 5:
        print(" Removing product...")
        delete_product(inventory)

    elif option == 6:
        print(" → Calculating statistics...")
        calculate_statistics(inventory)

    # ── TASK 4: Guardar CSV ─────────────────────────────────────
    elif option == 7:
        ruta = input(
            f" Ruta del archivo CSV (Enter para usar '{DEFAULT_CSV_PATH}'): "
        ).strip()
        if not ruta:
            ruta = DEFAULT_CSV_PATH
        guardar_csv(inventory, ruta)

    # ── TASK 5: Cargar CSV ──────────────────────────────────────
    elif option == 8:
        ruta = input(
            f" Ruta del archivo CSV a cargar (Enter para usar '{DEFAULT_CSV_PATH}'): "
        ).strip()
        if not ruta:
            ruta = DEFAULT_CSV_PATH
        inventory = gestionar_carga_csv(inventory, ruta)

    elif option == 9:
        print(" ╔════════════════════════════════════════════╗")
        print(" ║   ¡Thank you for using our INVENTORY!     ║")
        print(" ║   ¡Come back soon! 👋                     ║")
        print(" ╚════════════════════════════════════════════╝\n")
        break

    else:
        print(" Opción no válida. Elige entre 1 y 9.\n")