"""Write the current inventory data back to the storage file."""


def write_inventory(inventory):
    """Save the in-memory inventory dictionary to the inventory file.

    This method rewrites the whole file with the latest stock information so
    the data on disk always matches the application's current state.

    Parameters:
        inventory: A dictionary of products and their stock details.
    """
    try:
        # Rewrite the file completely to keep it consistent after sales,
        # restocking, or new purchases.
        with open("inventory.txt", "w") as file:
            for key, values in inventory.items():
                file.write(key)
                for value in values:
                    file.write(',' + str(value))
                file.write("\n")
    except Exception:
        print("Error while writing inventory to file.")