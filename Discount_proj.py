from datetime import date, datetime


discount_rate = 0.1
tax_rate = 0.06

today = datetime.now()
dow = today.weekday()

quantity = 1
subtotal = 0
while quantity != 0:
    quantity = int(input("Enter the quantity of the item (0 to stop): "))
    if quantity != 0:
        price = float(input("Enter the price of the item: "))
        subtotal += quantity * price
print(f"Subtotal: ${subtotal:.2f}")
discount = 0
if dow == 2 or dow == 3 :
    if subtotal >= 50:
        print("Discount applied: 10%")
        discount = subtotal * discount_rate
        print(f"Discount: ${discount:.2f}")
        subtotal -= discount
else:
    add_amount = 50 - subtotal
    print(f"Add ${add_amount:.2f} more to get a 10% discount.")
        




tax = subtotal * tax_rate
total_amount = subtotal + tax

print(f"Tax: ${tax:.2f}")
print(f"Total amount: ${total_amount:.2f}")
print(f"Subtotal after discount: ${subtotal:.2f}")

