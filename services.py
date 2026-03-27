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
        print(" No products in inventory to calculate statistics.\n")
        return
 
    # Lambda to calculate subtotal for each product
    subtotal = lambda p: p["price"] * p["quantity"]
 
    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)
    most_expensive_product = max(inventory, key=lambda p: p["price"])
    highest_stock_product = max(inventory, key=lambda p: p["quantity"])
 
    print("─" * 45)
    print("  INVENTORY STATISTICS")
    print("─" * 45)
    print(f"  Distinct products   : {len(inventory)}")
    print(f"  Total units         : {total_units}")
    print(f"  Total value         : ${total_value:,.2f}")
    print(f"  Most expensive      : {most_expensive_product['name']} "
          f"(${most_expensive_product['price']:.2f})")
    print(f"  Highest stock       : {highest_stock_product['name']} "
          f"({highest_stock_product['quantity']} units)")
    print("─" * 45)
    print("  Subtotal per product:")
    for p in inventory:
        print(f"   • {p['name']:<20} ${subtotal(p):>10,.2f}")
    print("─" * 45 + "\n")