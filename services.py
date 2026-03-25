
def add_product () :
    bu_n = True
    while bu_n :
        name = input ("ingresa nombre del product : ")
        if name:
            break
        else:
            print("El nombre del producto no puede estar vacío.")
    bu_p = True
    while bu_p :
        price = (input("ingresa preco del product : "))
        try:
            price = float(price)
            if price > 0:
                bu_p = False
            else:
                print(" The price must be greater than 0.")
        except ValueError:
            print(" You must enter a valid number for the price.")
    bu_q = True
    while bu_q :
        quantity = int(input("ingrese cantidad del product : "))
        try:
            quantity = int(quantity)
            if quantity > 0:
                bu_q = False
            else:
                print(" The quantity must be greater than 0.")
        except ValueError:
            print(" You must enter a valid integer for the quantity.")
    product = {
    "name"     : name ,
    "price"    : price ,
    "quantity" : quantity

    }
    return product


def search_product ():
    fdvdfv



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


def update_product (inventory) :
    for i in inventory :
        


def delete_product () :
    sadasdsad