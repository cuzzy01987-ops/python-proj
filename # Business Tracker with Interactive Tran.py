# Business Tracker with Interactive Transaction Prompts

from datetime import datetime

# Business constants
SELLING_PRICE = 85
COST_PRICE = 49
DAILY_SALES = 50



# --- Business Calculations ---
revenue = SELLING_PRICE * DAILY_SALES
cost = COST_PRICE * DAILY_SALES
gross_profit = revenue - cost
profit_percent = (gross_profit / cost) * 100

total_credits = sum(t["amount"] for t in transactions if t["type"] == ("credit"))
total_debits = sum(t["amount"] for t in transactions if t["type"] == ("debit"))
net_balance = total_credits - total_debits

# --- Report Display ---
print("\n====== WEEKLY BUSINESS REPORT ======")
print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
print("------------------------------------")
print(f"Units Sold: {DAILY_SALES}")
print(f"Total Revenue: Ksh {revenue}")
print(f"Total Cost: Ksh {cost}")
print(f"Gross Profit: Ksh {gross_profit}")
print(f"Profit Margin: {profit_percent:.1f}%")
print("------------------------------------")

# Transaction breakdown by category
print("\nTransaction Breakdown by Category:")
categories = ["profit", "loss", "sale", "expenditure"]
for cat in categories:
    filtered = [t for t in transactions if t["category"] == cat]
    if filtered:
        total = sum(t["amount"] for t in filtered)
        print(f"- {cat.title()} total: Ksh {total}")

print("\nCredit/Debit Summary:")
print(f"Total Credits: Ksh {total_credits}")
print(f"Total Debits: Ksh {total_debits}")
print(f"Net Credit Balance: Ksh {net_balance}")
print("------------------------------------")

print("\nPeople who OWE YOU money:")
for t in transactions:
    if t["type"] == "credit":
        print(f"  {t['name']} owes you Ksh {t['amount']} ({t['description']})")

print("\nPeople YOU OWE money to:")
for t in transactions:
    if t["type"] == "debit":
        print(f"  You owe {t['name']} Ksh {t['amount']} ({t['description']})")

print("------------------------------------")
total_week_balance = gross_profit + net_balance
print(f"Estimated Weekly Net Profit (after credits/debits): Ksh {total_week_balance}")
print("====================================")
