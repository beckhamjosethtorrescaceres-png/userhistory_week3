from services import *

inventory = [] #creacion de lista vacia para almacenar los productos
# Función para mostrar el menú principal
def show_menu(inventory):
    print("\n" + "═" * 60)
    print("       INVENTORY LIST MANAGEMENT - MAIN MENU")
    print("═" * 60)
    print("  1  →  Add product")
    print("  2  →  Show inventory")
    print("  3  →  search product")
    print("  4  →  update product")
    print("  5  →  delete product")
    print("  6  →  Calculate statistics")
    print("  7  →  Save CSV ")
    print("  8  →  Upload CSV")
    print("  9  →  Go out")
    print("═" * 60)
    # Programa principal
    print("╔══════════════════════════════════════╗")
    print("║     WELCOME TO THE INVENTORY         ║")
    print("╚══════════════════════════════════════╝\n")
op = True
while op:
        show_menu(inventory)
        try:
            option = int(input("  → Your choice: "))
            print() # línea en blanco para mejor lectura
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            continue
        except ValueError: #manejo de error si el usuario ingresa algo que no es un número
            print("  Error! You must enter a number (1-4).\n")
            continue
        except EOFError:
            print("\n\nProgram interrupted by user. Exiting...")
            continue


        if option == 1: 
            print("  → Adding product... ")
            product_info = add_product()
            inventory.append(product_info)
        elif option == 2:
            print("  → Showing inventory... ")
            for product in inventory:
                print(f"  - {product['name']}: ${product['price']:.2f} (quantity: {product['quantity']})")
        elif option == 3:
            print ("looking for product...")
        elif option == 4:
             print ("Updating product...")
             new_product = update_product(inventory)
        elif option == 5:
            print ("Removing product...")
        elif option == 6:
            print("  → Calculating statistics... ")
            calculate_statistics(inventory)

        elif option == 9:
            print("  ╔════════════════════════════════════════════╗")
            print("  ║   ¡Thank you for using our INVENTORY!      ║")
            print("  ║          ¡Come back soon! 👋               ║")
            print("  ╚════════════════════════════════════════════╝\n")
            print (inventory)
            break
        else:#manejo de error si el usuario ingresa un número que no corresponde a ninguna opción
            print("  Opción no válida. Elige entre 1 y 9.\n")