def validate_name(name):
    if not name:
        print("The name cannot be empty.")
        return False
    elif len(name) < 2:
        print("The name must be at least 2 characters long.")
        return False
    return True

def validate_price(price):
    try:
        price = float(price)
        if price <= 0:
            print("The price must be a positive number.")
            return False
        return True
    except ValueError:
        print("You must enter a valid number for the price.")
        return False

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("The quantity must be a positive integer.")
            return False
        return True
    except ValueError:
        print("You must enter a valid integer for the quantity.")
        return False