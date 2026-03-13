# Meal Price Calculator

# the price of child's meal
CHILD_MEAL_PRICE = float(input("Enter the price of a child's meal: "))

    

# the price of adult meal
ADULT_MEAL_PRICE = float(input("Enter the price of an adult meal: "))

# number of children
num_children = int(input("Enter the number of children: "))

# number of adults
num_adults = int(input("Enter the number of adults: "))

print()

# meal's subtotal for children
subtotal_children = CHILD_MEAL_PRICE * num_children
print(f"Subtotal for children's meals ({num_children} at ${CHILD_MEAL_PRICE} each): ${subtotal_children:.2f}")

# meal's subtotal for adults
subtotal_adults = ADULT_MEAL_PRICE * num_adults
print(f"Subtotal for adult's meals ({num_adults} at ${ADULT_MEAL_PRICE} each): ${subtotal_adults:.2f}")


#  meal's subtotal
subtota2 = subtotal_children + subtotal_adults
print(f"Total meal subtotal: ${subtota2:.2f}")
print()
 # Tax


#  sales tax
tax = 78
sales_tax = int(input("Enter the sales tax rate:"))
total_tax = tax * sales_tax


# total meal submition
total_subt = subtota2 + total_tax



# total meal cost
total_meal_cost = ADULT_MEAL_PRICE + CHILD_MEAL_PRICE
#  payment amount
payment_amount = float(input("Enter the payment amount: "))

    

# change
change = payment_amount - total_meal_cost
print(f"Change: ${change:.2f}")

