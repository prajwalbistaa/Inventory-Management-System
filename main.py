"""Main menu for the BuildMart hardware store management system."""

from read import read_inventory
from read import display_inventory
from transaction import sell_product 
from transaction import restock_inventory
from transaction import purchase_product

def main():
    """Run the store menu and manage the main user actions.

    The program loads the current inventory, shows the menu, and calls the
    related functions for viewing stock, selling goods, restocking items, or
    adding new purchases.
    """
    inventory = read_inventory("inventory.txt")

    while True:
        # Print the main menu each time the user returns to the program.
        print("\n")
        print("=" * 45)
        print("        BUILDMART HARDWARE STORE")
        print("=" * 45)
        print("1. Display Inventory")
        print("2. Sell Products")
        print("3. Restock Products")
        print("4. Purchase Products")
        print("5. Exit")
        print("=" * 45)

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\n"+"\n")
                display_inventory(inventory)
            elif choice == 2:
                print("\n")
                sell_product(inventory)
            elif choice == 3:
                print("\n")
                restock_inventory(inventory)
            elif choice == 4:
                print("\n")
                purchase_product()
            elif choice == 5:
                print("\nThank You for shopping at BuildMart Hardware Store.")
                print("Have a Nice Day!\n")
                break
            else:
                print("\nInvalid Choice!")
                print("Please Enter a Number Between 1 and 5.")
        except ValueError:
            print("\nInvalid Input!")
            print("Please Enter a Valid Number.")

main()
