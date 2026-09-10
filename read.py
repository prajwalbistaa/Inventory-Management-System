"""Load and display inventory data from the inventory file."""


def read_inventory(filepath):
    """Read the inventory file and convert it into a dictionary.

    Each product line in the file is stored as a comma-separated record:
    product id, product name, brand, stock, unit, and rate.

    Parameters:
        filepath: The file path to the inventory data file.

    Returns:
        A dictionary where each key is a product id and each value is the
        product details in list form.
    """
    inventory_dict = {}
    try:
        # Read every line and convert it into a structured inventory record.
        with open(filepath) as file:
            products = file.readlines()
            for product in products:
                if not product.strip(): 
                    continue
                item = product.strip().split(",")
                inventory_dict[item[0]] = [item[1], item[2], int(item[3]), item[4], float(item[5])]
    except FileNotFoundError:
        print("No inventory file was found.")
    return inventory_dict


def display_inventory(inventory):
    """Print the inventory in a clean tabular format for the user."""
    # Show the inventory table header for an easy-to-read console display.
    print(f'{"ID":<8}{"Product Name":<20}{"Brand":<20}{"Stock":<10}{"Unit":<10}{"Rate":<10}')
    print("-" * 75)
    for key, value in inventory.items():
        print(f' {key:<8}{value[0]:<20}{value[1]:<20}{value[2]:<10}{value[3]:<10}{value[4]:<10}')
