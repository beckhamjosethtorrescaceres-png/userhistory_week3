from validations import *

def add_product():
    bu_n = True
    bu_p = True
    bu_q = True

    while bu_n:
        name = input("Enter product name: ").strip()
        if validate_name(name):
            bu_n = False

    while bu_p:
        price = input("Enter product price: ")
        if validate_price(price):
            price = float(price)  
            bu_p = False

    while bu_q:
        quantity = input("Enter product quantity: ")
        if validate_quantity(quantity):
            quantity = int(quantity) 
            bu_q = False

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    return product
##############################################################   
def update_product(inventory):
    if not inventory:
        print("No products in inventory")
        return

    running = True

    while running:
        for i, product in enumerate(inventory):
            print(f"{i + 1} -> {product['name']} : ${product['price']:.2f} (quantity: {product['quantity']})")

        choice = input("Select product number (or 'exit' to quit): ").strip()

        if choice.lower() == "exit":
            print("Exiting...")
            running = False
            continue

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        index = int(choice) - 1
        if not (0 <= index < len(inventory)):
            print("Invalid index")
            continue

        bu_n = True
        bu_p = True
        bu_q = True


        while bu_n:
            new_name = input("New name (press Enter to keep current): ").strip()
            if not new_name or validate_name(new_name):
                bu_n = False


        while bu_p:
            new_price = input("New price (press Enter to keep current): ").strip()
            if not new_price or validate_price(new_price):
                if new_price:
                    new_price = float(new_price)
                bu_p = False
                
        while bu_q:
            new_quantity = input("New quantity (press Enter to keep current): ").strip()
            if not new_quantity or validate_quantity(new_quantity):
                if new_quantity:
                    new_quantity = int(new_quantity)
                bu_q = False
        if new_name:
            inventory[index]["name"] = new_name
        if new_price:
            inventory[index]["price"] = new_price
        if new_quantity:
            inventory[index]["quantity"] = new_quantity
        updated_product = inventory[index]
        print("Product updated successfully")
        print(f"Updated product -> {updated_product['name']} : ${updated_product['price']:.2f} (quantity: {updated_product['quantity']})\n")

        running = False
##############################################################       
def delete_product(inventory):
    if not inventory:
        print("No products in inventory")
        return

    bu = True
    while bu:
        for i, product in enumerate(inventory):
            print(f"  {i + 1} → {product['name']} : ${product['price']:.2f} (quantity: {product['quantity']})")

        choice = input("Choose the number of the product to delete (or 'exit' to cancel): ").strip()

        if choice.lower() == "exit":
            print("Operation cancelled.")
            bu = False
            continue

        if not choice.isdigit():
            print("Please, enter a valid number.")
            continue

        index = int(choice) - 1

        if not (0 <= index < len(inventory)):
            print("Number out of range. Please try again.")
            continue

        deleted_product = inventory.pop(index)
        print(f"Product '{deleted_product['name']}' deleted successfully.")
        bu = False