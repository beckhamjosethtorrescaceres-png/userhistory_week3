import csv
import os
from validations import *

import csv

# ── Constants ──────────────────────────────────────────────────
HEADER = ["name", "price", "quantity"]


def save_to_csv(inventory: list[dict], filepath: str, include_header: bool = True) -> None:
    """
    Save the inventory to a CSV file with comma separator.
    
    Args:
        inventory: List of product dictionaries to save
        filepath: Path where the CSV file will be written
        include_header: Whether to write the header row (default: True)
    
    Returns:
        None
    """

    if not inventory:
        print("  The inventory is empty. Nothing to save.\n")
        return

    try:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if include_header:
                writer.writerow(HEADER)

            for product in inventory:
                writer.writerow([
                    product["name"],
                    product["price"],
                    product["quantity"],
                ])

        print(f" ✔  Inventory saved to: {filepath}\n")

    except PermissionError:
        print(f" ✘  Permission denied to write to '{filepath}'. "
              "Please check the file path or permissions.\n")
    except OSError as e:
        print(f" ✘  Error saving file: {e}\n")


def load_from_csv(filepath: str) -> list[dict] | None:
    """
    Read a CSV file and return a list of products.
    Returns None if the file cannot be opened or the header is invalid.
    Rows with errors are skipped and an error counter is accumulated.
    
    Args:
        filepath: Path to the CSV file to load
        
    Returns:
        list[dict]: List of valid products loaded, or None if critical error
    """

    products = []
    invalid_rows = 0

    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            # ── Validate header ──────────────────────────────
            try:
                header = next(reader)
            except StopIteration:
                print("  The file is empty.\n")
                return None

            header_normalized = [col.strip().lower() for col in header]
            if header_normalized != HEADER:
                print(
                    f"  Invalid header: {header_normalized}\n"
                    f"   Expected: {HEADER}\n"
                )
                return None

            # ── Read rows ──────────────────────────────────────
            for row_num, row in enumerate(reader, start=2):  # start=2 (row 1 = header)

                # 1. Exactly 3 columns
                if len(row) != 3:
                    invalid_rows += 1
                    continue

                name, price_raw, quantity_raw = (col.strip() for col in row)

                # 2. Validate name
                if not validate_name(name):
                    invalid_rows += 1
                    continue

                # 3. Validate price
                if not validate_price(price_raw):
                    invalid_rows += 1
                    continue
                price = float(price_raw)

                # 4. Validate quantity
                if not validate_quantity(quantity_raw):
                    invalid_rows += 1
                    continue
                quantity = int(quantity_raw)

                products.append({
                    "name": name,
                    "price": price,
                    "quantity": quantity,
                })

    except FileNotFoundError:
        print(f"  File not found: '{filepath}'\n")
        return None
    except UnicodeDecodeError:
        print(f"  The file '{filepath}' has an incompatible encoding. "
              "Please save it as UTF-8 and try again.\n")
        return None
    except ValueError as e:
        print(f"   Unexpected value error while reading CSV: {e}\n")
        return None
    except Exception as e:
        print(f"  Unexpected error reading '{filepath}': {e}\n")
        return None

    if invalid_rows:
        print(f"  {invalid_rows} invalid row(s) skipped.")

    return products


def _merge(inventory: list[dict], new_products: list[dict]) -> tuple[list[dict], int]:
    """
    Merge policy:
      - If product name already exists → add quantities and update price to new value.
      - If name doesn't exist → append the new product.
      
    Args:
        inventory: Current inventory list
        new_products: List of products loaded from CSV
        
    Returns:
        tuple: (merged_inventory_list, count_of_updated_products)
    """
    updated_count = 0
    inventory_copy = [p.copy() for p in inventory]

    for new_item in new_products:
        name_lower = new_item["name"].lower()
        existing = next(
            (p for p in inventory_copy if p["name"].lower() == name_lower),
            None,
        )
        if existing:
            existing["quantity"] += new_item["quantity"]
            existing["price"] = new_item["price"]
            updated_count += 1
        else:
            inventory_copy.append(new_item)

    return inventory_copy, updated_count


def manage_csv_load(inventory: list[dict], filepath: str) -> list[dict]:
    """
    Orchestrates CSV loading and the overwrite/merge decision.
    Returns the resulting inventory (modified or unchanged).
    
    Args:
        inventory: Current inventory list
        filepath: Path to the CSV file to load
        
    Returns:
        list[dict]: The resulting inventory after load operation
    """

    new_products = load_from_csv(filepath)

    if new_products is None:
        return inventory  # Unrecoverable error; don't change anything

    if not new_products:
        print("  The file contains no valid products.\n")
        return inventory

    # ── Ask user for decision ────────────────────────────────────
    print(f"\n Found {len(new_products)} valid product(s) in '{filepath}'.")
    print(
        "\n Merge policy (option N):\n"
        "   • If name already exists → quantity is added and price is updated.\n"
        "   • If name is new         → product is added to inventory.\n"
    )
    
    while True:
        response = input(" Overwrite current inventory? (Y/N): ").strip().upper()
        if response in ("Y", "N"):
            break
        print(" Please enter Y or N.")

    if response == "Y":
        result_inventory = new_products
        action = "Full replacement"
        updated_count = 0
    else:
        result_inventory, updated_count = _merge(inventory, new_products)
        action = "Merge"

    # ── Summary ────────────────────────────────────────────────
    print("\n" + "─" * 50)
    print(f"  Action            : {action}")
    print(f"  Products loaded   : {len(new_products)}")
    if response == "N":
        print(f"  Products updated (merge): {updated_count}")
    print(f"  Total in inventory: {len(result_inventory)}")
    print("─" * 50 + "\n")

    return result_inventory