"""Handle product sales, restocking, and purchase transactions."""

from read import display_inventory, read_inventory
from write import write_inventory
from append import append_inventory
from invoice import restock_invoice, sale_invoice, purchase_invoice
import datetime 

def sell_product(inventory):
    """Process a customer sale and update the stock list in memory.

    The function validates the product, checks stock quantity, calculates the
    discount and total, and then writes the updated inventory back to disk.

    Args:
        inventory: The complete inventory dictionary currently in use.
    """
    sold_items = []
    final_price = 0
    display_inventory(inventory)

    while True:
        name = input("\nEnter Customer Name: ")
        if not name.strip():
            print("Customer Name cannot be empty.")
            continue
        else:
            break

    while True:
        id = input("Enter Product ID: ")
        if id not in inventory:
            print("Invalid Product ID !")
            continue
        product = inventory[id]
        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                if quantity > int(product[2]):
                    print("Insufficient Stock.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid Quantity.")
        
        price = float(product[4])
        subtotal = quantity * price
        discount = 0

        if product[3].strip().lower() == "kg":
            if quantity >= 50:
                discount = subtotal * 0.05
        elif product[3].strip().lower() == "quantity":
            if quantity >= 100:
                discount = subtotal * 0.05

        total = subtotal - discount

        inventory[id][2] -= quantity
        final_price += total
        sold_items.append([product[0], quantity, price,subtotal, discount, total])

        while True:
            choice = input("Do you want to add another product? (Y/N): ").upper()
            if choice == "Y" or choice == "YES":
                break
            elif choice == "N" or choice == "NO":
                print("\n" + "=" * 85)
                print("SALES BILL")
                print("=" * 85)
                print("Customer Name: ", name)
                print("Date: ", datetime.datetime.now().strftime("%Y-%m-%d"))
                print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"))
                print("-" * 85)
                print(f'{"Product":<22}{"Quantity":<15}{"Price":<15}{"Discount":<15}{"Final Cost":<15}')
                print("-" * 85)

                for item in sold_items:
                    item_name = item[0]
                    quantity_and_type = str(item[1]) + " " + str(product[3])
                    item_price = item[3]
                    item_discount = item[4]
                    item_final_cost = item[5]

                    print(f'{item_name:<22}{quantity_and_type:<15}{("Rs." + str(round(item_price, 2))):<15}{("Rs." + str(round(item_discount, 2))):<15}{("Rs." + str(round(item_final_cost, 2))):<15}')

                print("-" * 85)
                total_discount = sum(item[4] for item in sold_items)
                print(f'{"TOTAL":<37}{("Rs." + str(round(final_price + total_discount, 2))):<15}{("Rs." + str(round(total_discount, 2))):<15}{("Rs." + str(round(final_price, 2))):<15}')
                print("=" * 85)
                sale_invoice(name, sold_items, final_price)
                write_inventory(inventory)
                return
            else:
                print("Invalid Choice !")


def restock_inventory(inventory):
    """Add stock to existing products and generate a restock summary."""
    restocked_items = []
    total_price = 0
    display_inventory(inventory)

    while True:
        name = input("\nEnter Vendor Name: ")
        if not name.strip():
            print("Vendor Name cannot be empty.")
            continue
        else:
            break

    while True:
        id = input("Enter Product ID: ")
        if id not in inventory:
            print("Invalid Product ID !")
            continue
        product = inventory[id]
        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid Quantity.")
        
        price = float(product[4])
        sub_price = quantity * price
        total_price += sub_price 

        inventory[id][2] += quantity

        restocked_items.append([product[0],quantity,price,sub_price])

        while True:
            choice = input("Do want to restock another product? (Y/N): ").upper()
            if choice == "Y" or choice == "YES":
                break
            elif choice == "N" or choice == "NO":
                discount = total_price * 0.10
                final_price = total_price - discount
                print("\n" + "=" * 85)
                print("RESTOCK BILL")
                print("=" * 85)
                print("Vendor Name: ", name)
                print("Date: ", datetime.datetime.now().strftime("%Y-%m-%d"))
                print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"))
                print("-" * 85)
                print(f'{"Product":<22}{"Quantity":<15}{"Price":<15}{"Discount":<15}{"Final Cost":<15}')
                print("-" * 85)

                for item in restocked_items:
                    item_name = item[0]
                    quantity_and_type = str(item[1]) + " " + str(product[3])
                    item_price = item[3]
                    item_discount = item_price * 0.10
                    item_final_cost = item_price - item_discount

                    print(f'{item_name:<22}{quantity_and_type:<15}{("Rs." + str(round(item_price, 2))):<15}{("Rs." + str(round(item_discount, 2))):<15}{("Rs." + str(round(item_final_cost, 2))):<15}')

                print("-" * 85)
                print(f'{"TOTAL":<37}{("Rs." + str(round(total_price, 2))):<15}{("Rs." + str(round(discount, 2))):<15}{("Rs." + str(round(final_price, 2))):<15}')
                print("=" * 85)
                restock_invoice(name, restocked_items,total_price, discount, final_price)
                write_inventory(inventory)
                return
            else:
                print("Invalid Choice !")


def purchase_product():
    """Record a purchase from a supplier and save the new inventory items."""
    purchased_items = []
    final_price = 0
    total_price = 0
    
    while True:
        vendor_name = input("Enter Vendor Name: ")
        if not vendor_name.strip():
            print("Vendor Name cannot be empty.")
            continue
        else:
            break

    def product_id(inventory):
        """Generate the next product id for a newly purchased item."""
        if not inventory:
            return "I1"
        last_id = list((int(id[1:]) for id in inventory.keys()))
        new_id = "I" + str(last_id[-1] + 1)
        return new_id
    
    while True:
        while True:
            name = input("Enter Product Name: ")
            if not name.strip():
                print("Product Name cannot be empty.")
                continue
            break

        while True:
            brand = input("Enter Product Brand: ")
            if not brand.strip():
                print("Product Brand cannot be empty.")
                continue
            break

        while True:
            unit = input("Enter Product Unit (kg/quantity): ")
            if unit.strip().lower() not in ["kg", "quantity"]:
                print("Unit must be either 'kg' or 'quantity'.")
                continue
            break

        while True:
            try:
                quantity = int(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid Quantity.")

        while True:
            try:
                price = float(input("Enter Product Price: "))
                if price <= 0:
                    print("Price must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid Price.")      

        sub_price = quantity * price
        total_price += sub_price 

        id = product_id(inventory = read_inventory("inventory.txt"))

        purchased_items.append([id, name, brand, unit, quantity, price, sub_price])
        append_inventory({id : [name, brand, quantity, unit, price]})

        while True:
            choice = input("Do want to add another product? (Y/N): ").upper()
            if choice == "Y" or choice == "YES":
                break
            elif choice == "N" or choice == "NO":
                discount = total_price * 0.10
                final_price = total_price - discount
                print("\n" + "=" * 70)
                print("PURCHASE BILL")
                print("=" * 70)
                print("Vendor Name: ", vendor_name)
                print("Date: ", datetime.datetime.now().strftime("%Y-%m-%d"))
                print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"))
                print("-" * 70)
                print(f'{"Product":<22}{"Quantity":<15}{"Rate":<15}{"Total":<15}')
                print("-" * 70)

                for item in purchased_items:
                    item_name = item[1]
                    quantity_and_type = str(item[4]) + " " + str(item[3])
                    item_price = item[6]

                    print(f'{item_name:<22}{quantity_and_type:<15}{("Rs." + str(round(price, 2))):<15}{("Rs." + str(round(item_price, 2))):<15}')

                print("-" * 70)
                print(f'{"SUBTOTAL":<22}{("Rs." + str(round(total_price, 2))):<15}')
                print(f'{"DISCOUNT":<22}{("Rs." + str(round(discount, 2))):<15}')
                print(f'{"GRAND TOTAL":<22}{("Rs." + str(round(final_price, 2))):<15}')
                print("=" * 70)
                purchase_invoice(vendor_name, purchased_items,total_price, discount, final_price)
                return
            else:
                print("Invalid Choice !")
