from validations import *

def search_product (inventory):
    if not inventory:
        print("No products in inventory")
        return

    search_name = input("Enter product name to search: ").strip().lower()

    found_products = [p for p in inventory if search_name in p['name'].lower()]
    if found_products:
        for product in found_products:
            print(f"  - {product['name']}: ${product['price']:.2f} (quantity: {product['quantity']})")
    else:
        print("  Product not found in inventory.\n")



def calculate_statistics(inventory: list[dict]) -> None:
    if not inventory:
        print(" No hay productos en el inventario para calcular estadísticas.\n")
        return
 
    # Lambda para calcular el subtotal de cada producto
    subtotal = lambda p: p["price"] * p["quantity"]
 
    unidades_totales  = sum(p["quantity"] for p in inventory)
    valor_total       = sum(subtotal(p) for p in inventory)
    producto_mas_caro = max(inventory, key=lambda p: p["price"])
    producto_mayor_stock = max(inventory, key=lambda p: p["quantity"])
 
    print("─" * 45)
    print("  ESTADÍSTICAS DEL INVENTARIO")
    print("─" * 45)
    print(f"  Productos distintos : {len(inventory)}")
    print(f"  Unidades totales    : {unidades_totales}")
    print(f"  Valor total         : ${valor_total:,.2f}")
    print(f"  Producto más caro   : {producto_mas_caro['name']} "
          f"(${producto_mas_caro['price']:.2f})")
    print(f"  Mayor stock         : {producto_mayor_stock['name']} "
          f"({producto_mayor_stock['quantity']} unidades)")
    print("─" * 45)
    print("  Subtotal por producto:")
    for p in inventory:
        print(f"   • {p['name']:<20} ${subtotal(p):>10,.2f}")
    print("─" * 45 + "\n")


