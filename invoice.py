"""Generate sales, restock, and purchase invoices for the store."""

import datetime
 
def sale_invoice(name, sold_items, final_price):
    """Create a sales invoice file for a customer purchase.

    Parameters:
        name: Customer name.
        sold_items: List of product entries sold in the transaction.
        final_price: Final payable amount after discount.
    """
    invoice_number = "INV" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    filename = "Sales_" + invoice_number + ".txt"

    try:
        # Build the invoice text using a fixed-width layout for readability.
        with open(filename, "w") as file:
            file.write("============================================================================================\n")
            file.write("                                 BUILDMART HARDWARE STORE\n")
            file.write("                                       SALES INVOICE\n")
            file.write("============================================================================================\n\n")

            file.write("Invoice Number : " + invoice_number + "\n")
            file.write("Customer Name  : " + name + "\n")
            file.write("Date           : " + date + "\n")
            file.write("Time           : " + time + "\n\n")

            file.write("--------------------------------------------------------------------------------------------\n")
            file.write(f'{"Product Name":<20}{"Quantity":<15}{"Rate":<15}{"Subtotal":<15}{"Discount":<15}{"Total":<15}\n')
            file.write("--------------------------------------------------------------------------------------------\n")

            for item in sold_items:
                file.write(f'{item[0]:<20}{str(item[1]):<15}{"Rs." + str(item[2]):<15}{"Rs." + str(round(item[3], 2)):<15}{"Rs." + str(round(item[4], 2)):<15}{("Rs." + str(round(item[5], 2))):<15}\n')

            file.write("--------------------------------------------------------------------------------------------\n")
            file.write("Grand Total : Rs. " + str(round(final_price, 2)) + "\n")
            file.write("============================================================================================\n")
            file.write("                          Thank You For Shopping With BuildMart!\n")
            file.write("============================================================================================\n")

        print("\nSales Invoice Generated Successfully.")
        print("Saved As:", filename)
    except Exception:
        print("Error while generating sales invoice.")


def restock_invoice(name, restocked_items, total_price, discount, final_price):
    """Create a supplier restock invoice for incoming inventory.

    Parameters:
        name: Supplier or vendor name.
        restocked_items: Items being restocked.
        total_price: Raw subtotal before discount.
        discount: Discount amount applied to the purchase.
        final_price: Final amount payable after discount.
    """
    invoice_number = "INV" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    filename = "Restock_" + invoice_number + ".txt"

    try:
        with open(filename, "w") as file:
            file.write("============================================================================================\n")
            file.write("                                 BUILDMART HARDWARE STORE\n")
            file.write("                                       RESTOCK INVOICE\n")
            file.write("============================================================================================\n\n")

            file.write("Invoice Number : " + invoice_number + "\n")
            file.write("Supplier Name  : " + name + "\n")
            file.write("Date           : " + date + "\n")
            file.write("Time           : " + time + "\n\n")

            file.write("--------------------------------------------------------------------------------------------\n")
            file.write(f'{"Product Name":<20}{"Quantity":<15}{"Rate":<15}{"Total":<15}\n')
            file.write("--------------------------------------------------------------------------------------------\n")

            for item in restocked_items:
                file.write(f'{item[0]:<20}{str(item[1]):<15}{"Rs." + str(item[2]):<15}{"Rs." + str(round(item[3], 2)):<15}\n')

            file.write("--------------------------------------------------------------------------------------------\n")
            file.write("Sub Total : Rs. " + str(round(total_price, 2)) + "\n")
            file.write("Discount    : Rs. " + str(round(discount, 2)) + "\n")
            file.write("Grand Total : Rs. " + str(round(final_price, 2)) + "\n")
            file.write("============================================================================================\n")
            file.write("                                 Restocking For BuildMart!\n")
            file.write("============================================================================================\n")

        print("\nRestock Invoice Generated Successfully.")
        print("Saved As:", filename)
    except Exception:
        print("Error while generating restock invoice.")


def purchase_invoice(name, purchased_items, total_price, discount, final_price):
    """Create a purchase invoice for products bought from a supplier.

    Args:
        name: Supplier or vendor name.
        purchased_items: Items included in the purchase transaction.
        total_price: Total before discount.
        discount: Discount applied to the transaction.
        final_price: Net payable amount after discount.
    """
    invoice_number = "INV" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    filename = "Purchase_" + invoice_number + ".txt"

    try:
        with open(filename, "w") as file:
            file.write("=====================================================================================================\n")
            file.write("                                 BUILDMART HARDWARE STORE\n")
            file.write("                                       PURCHASE INVOICE\n")
            file.write("=====================================================================================================\n\n")

            file.write("Invoice Number : " + invoice_number + "\n")
            file.write("Supplier Name  : " + name + "\n")
            file.write("Date           : " + date + "\n")
            file.write("Time           : " + time + "\n\n")

            file.write("-----------------------------------------------------------------------------------------------------\n")
            file.write(f'{"Product ID":<15}{"Product Name":<20}{"Brand":<15}{"Unit":<10}{"Quantity":<15}{"Rate":<15}{"Total":<15}\n')
            file.write("-----------------------------------------------------------------------------------------------------\n")

            for item in purchased_items:
                file.write(f'{item[0]:<15}{item[1]:<20}{item[2]:<15}{str(item[3]):<15}{item[4]:<10}{"Rs." + str(item[5]):<15}{"Rs." + str(item[6]):<15}\n')

            file.write("-----------------------------------------------------------------------------------------------------\n")
            file.write("Sub Total : Rs. " + str(round(total_price, 2)) + "\n")
            file.write("Discount    : Rs. " + str(round(discount, 2)) + "\n")
            file.write("Grand Total : Rs. " + str(round(final_price, 2)) + "\n")
            file.write("=====================================================================================================\n")
            file.write("                                 Purchase For BuildMart!\n")
            file.write("=====================================================================================================\n")

        print("\nPurchase Invoice Generated Successfully.")
        print("Saved As:", filename)
    except Exception:
        print("Error while generating purchase invoice.")
