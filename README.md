# BuildMart Hardware Store

BuildMart is a command-line hardware store management system written in Python. It keeps product stock in a text file, supports sales and supplier transactions, and generates text invoices for completed transactions.

## Features

- Display the current inventory.
- Sell one or more products in a single customer transaction.
- Restock existing products from a vendor.
- Add newly purchased products to the inventory.
- Apply transaction discounts:
  - Sales: 5% for at least 50 kg or 100 units of an eligible product.
  - Restocking and purchases: 10% of the transaction subtotal.
- Update `inventory.txt` after sales and restocking.
- Generate sales, restock, and purchase invoices as `.txt` files.

## Requirements

- Python 3.8 or newer
- No external packages are required.

## Project Structure

| File             | Purpose                                               |
| ---------------- | ----------------------------------------------------- |
| `main.py`        | Starts the application and displays the main menu.    |
| `read.py`        | Reads and displays inventory data.                    |
| `write.py`       | Rewrites `inventory.txt` after stock changes.         |
| `append.py`      | Appends newly purchased products to `inventory.txt`.  |
| `transaction.py` | Handles sales, restocking, and new product purchases. |
| `invoice.py`     | Creates sales, restock, and purchase invoice files.   |
| `inventory.txt`  | Stores the current product inventory.                 |

## Running the Application

Open a terminal in the project directory and run:

```bash
python main.py
```

On some Windows installations, use:

```bash
py main.py
```

The application displays this menu:

1. Display Inventory
2. Sell Products
3. Restock Products
4. Purchase Products
5. Exit

Follow the prompts to enter customer or vendor details, product IDs, quantities, and prices. Enter `Y` or `YES` to add another product to the current transaction, or `N` or `NO` to complete it.

## Inventory File Format

Each non-empty line in `inventory.txt` represents one product using six comma-separated fields:

```text
product_id, product_name, brand, stock, unit, rate
```

Example:

```text
I1, Cement OPC, Shivam Cement,980, kg,12.0
```

The supported units are `kg` and `quantity`. Product IDs are generated in sequence when new products are added.

## Generated Files

Completed transactions create invoice files in the project directory:

- `Sales_INV<timestamp>.txt`
- `Restock_INV<timestamp>.txt`
- `Purchase_INV<timestamp>.txt`

The inventory file is modified in place after sales and restocking. New product purchases are appended to it.

## Important Notes

- Run the program from the project directory so it can find `inventory.txt` and save invoices in the expected location.
- Keep the inventory file in the six-field format described above.
- Make a backup of `inventory.txt` before manually editing or testing stock changes.
