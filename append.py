"""Append new inventory entries to the inventory file."""


def append_inventory(inventory):
    """Add newly created products to the existing inventory file.

    The function keeps the current file content and appends the new records
    at the end, so previous stock entries remain intact.

    Parameters:
        inventory: A dictionary of product ids mapped to their inventory data.
    """
    try: 
        # Open the file in append mode so we do not overwrite earlier records.
        with open("inventory.txt", "a") as file:
            for key, values in inventory.items():
                file.write("\n")
                file.write(key)
                for value in values:
                    file.write(', ' + str(value))
    except Exception:
        print("Error while appending inventory to file.")
