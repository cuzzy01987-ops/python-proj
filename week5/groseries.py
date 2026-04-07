
    
    
import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """Read a CSV file and return a dictionary."""
    products_dict = {}

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            key = row[key_column_index]
            products_dict[key] = row

    return products_dict


def main():
    try:
        print("Welcome to Uncle's Grocery Store")
        print("-" * 35)

        # Read product catalog
        products_dict = read_dictionary("products.csv", 0)

        subtotal = 0
        total_items = 0

        # Read customer order
        with open("request.csv", "r") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header

            print("\nItems Ordered:")

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                # Look up product
                product = products_dict[product_number]
                product_name = product[1]
                price = float(product[2])

                item_total = price * quantity

                print(f"{product_name}: {quantity} @ {price:.2f}")

                subtotal += item_total
                total_items += quantity

        # Calculate tax and total
        tax = subtotal * 0.06
        total = subtotal + tax

        print("\n" + "-" * 35)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")

        # Print date and time
        now = datetime.now()
        print("\nThank you for shopping with us!")
        print(now.strftime("%A %B %d, %Y %I:%M %p"))

    except FileNotFoundError as err:
        print("Error: Missing file")
        print(err)

    except PermissionError as err:
        print("Error: Permission denied")
        print(err)

    except KeyError as err:
        print("Error: Unknown product ID in request file")
        print(err)


if __name__ == "__main__":
    main()