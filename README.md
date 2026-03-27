# userhistory_week3
# Inventory List Management

A console-based inventory management system built in Python. It allows you to add, view, update, and delete products, calculate statistics, and save or load the inventory from CSV files.

---

## Project Structure

```
userhistory_week3/
├── app.py           # Entry point — main menu and program flow
├── CRUD.py          # Create, update, and delete operations
├── services.py      # Product search and statistics calculation
├── CSV.py           # Save and load inventory in CSV format
└── validations.py   # Name, price, and quantity validations
```

---

## Requirements

- Python 3.10 or higher
- No external libraries required (uses only standard library modules: `csv`, `os`)

---

## How to Run

```bash
python app.py
```

---

## Main Menu

When the program starts, you will see the following menu:

```
============================================================
 INVENTORY LIST MANAGEMENT - MAIN MENU
============================================================
 1 -> Add product
 2 -> Show inventory
 3 -> Search product
 4 -> Update product
 5 -> Delete product
 6 -> Calculate statistics
 7 -> Save CSV
 8 -> Upload CSV
 9 -> Go out
============================================================
```

---

## Features

### 1. Add Product
Prompts for name, price, and quantity. Each field is validated before being accepted.

### 2. Show Inventory
Lists all stored products with their name, price, and quantity.

### 3. Search Product
Searches by name (case-insensitive). Displays all matching products.

### 4. Update Product
Shows the numbered inventory and allows editing the name, price, or quantity of a product. Pressing Enter without typing keeps the current value.

### 5. Delete Product
Shows the numbered inventory and removes the selected product.

### 6. Calculate Statistics
Displays:
- Total number of units in inventory
- Total inventory value (price x quantity per product)

### 7. Save CSV
Exports the current inventory to a `.csv` file at the path you specify. The file will include the header `nombre,precio,cantidad`.

Example of a generated file:
```
nombre,precio,cantidad
Laptop,1500.0,3
Mouse,25.5,10
```

### 8. Upload CSV
Loads products from a `.csv` file. When loading, the program asks whether you want to:

- Overwrite (S): replaces the entire current inventory with the data from the file.
- Merge (N): if a product from the CSV already exists in the inventory, its quantity is added and its price is updated. If it is new, it is appended.

The file must have exactly the header `nombre,precio,cantidad`. Rows with invalid data are skipped automatically and the number of discarded rows is reported.

### 9. Exit
Closes the program with a farewell message.

---

## Validations

All inputs go through `validations.py` before being accepted:

| Field    | Rules                                          |
|----------|------------------------------------------------|
| Name     | Cannot be empty, minimum 2 characters          |
| Price    | Must be a number greater than 0                |
| Quantity | Must be a positive integer greater than 0      |

If the user enters an invalid value, the program notifies them and prompts for the input again.

---

## Module Architecture

```
app.py
 ├── CRUD.py
 │    └── validations.py
 ├── services.py
 │    └── validations.py
 └── CSV.py
      └── validations.py
```

Each module imports only what it needs from `validations.py`, keeping responsibilities clearly separated.

---

## Author

Beckham Torres Caceres
https://github.com/beckhamjosethtorrescaceres-png
