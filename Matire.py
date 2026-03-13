# Small Business Tracker: sales, credits, debits, expenses, and profits

from datetime import datetime
# business setup
business_name = "Matire"
business_address = "NE_Darfur, Sudan"
business_phone = "+249912345678"

# financial records
sales = []
credits = []
debits = []
expenses = []
profits = []
# functions to add records
def add_sale(amount, description):
    sales.append({"amount": amount, "description": description, "date": datetime.now()})
def add_credit(amount, description):
    credits.append({"amount": amount, "description": description, "date": datetime.now()})
def add_debit(amount, description):
    debits.append({"amount": amount, "description": description, "date": datetime.now()})
def add_expense(amount, description):
    expenses.append({"amount": amount, "description": description, "date": datetime.now()})
def calculate_profit():
    total_sales = sum(sale["amount"] for sale in sales)
    total_credits = sum(credit["amount"] for credit in credits)
    total_debits = sum(debit["amount"] for debit in debits)
    total_expenses = sum(expense["amount"] for expense in expenses)
    profit = (total_sales + total_credits) - (total_debits + total_expenses)
    profits.append({"amount": profit, "date": datetime.now()})
    return profit
# example usage
add_sale(1000, "Sale of product A")
add_credit(200, "Customer refund")
add_debit(150, "Purchase of supplies")
add_expense(300, "Monthly rent")
current_profit = calculate_profit()
print(f"Current profit for {business_name}: ${current_profit}")
