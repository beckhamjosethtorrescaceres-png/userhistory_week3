from validations import *

def search_product (inventory):
    if not inventory:
        print("No products in inventory")
        return

    search_name = input("Enter product name to search: ").strip().lower()

    found_products = [product for product in inventory if product['name'].lower() == search_name]

    if found_products:
        for product in found_products:
            print(f"  - {product['name']}: ${product['price']:.2f} (quantity: {product['quantity']})")
    else:
        print("  Product not found in inventory.\n")



def calculate_statistics(inventory):
    len_inventory = len(inventory)#obtener la cantidad de productos en el inventario
    
    if len_inventory == 0:#manejo de error si el inventario está vacío
        
        print("  No hay productos en el inventario para calcular estadísticas.\n")
        return#salir de la función si no hay productos en el inventario
    
    else:#calcular estadísticas si hay productos en el inventario
        
        prices = [product['price'] for product in inventory]#crear una lista de precios a partir del inventario
        
        quantitys = [product['quantity'] for product in inventory]
        
        price_total = sum(prices)#calcular el precio total sumando todos los precios de los productos en el inventario
        quantity_total = sum(quantitys)
        
        #calcular el valor total del inventario multiplicando el precio por la cantidad de cada producto y sumando los resultados
        total_inventory_value = sum(product['price'] * product['quantity'] for product in inventory)

        print(f"  → Cantidad total de productos: {quantity_total}")
        print(f"  → Valor total del inventario: ${total_inventory_value:.2f}\n")


