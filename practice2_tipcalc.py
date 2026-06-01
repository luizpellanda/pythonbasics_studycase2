# Restaurant Tip Calculator

# A utility for waitstaff to quickly calculate gratuity and total bill amounts based on custom tip percentages.

# * **Inputs:** Bill amount, tip percentage (default suggested: 10%).
# * **Outputs:** Calculated tip value and final total amount to be charged.


def calc_tip(tip_percentage, bill_amount):
    tip_calculated = bill_amount * (tip_percentage * 0.01)
    total = bill_amount + tip_calculated
    print(f"Tip amount is ${tip_calculated:.2f}")
    print(f"Total bill is ${total:.2f}")

print("Restaurant Tip Calculator")

try:
    bill = float(input("Please type the bill amount: "))
    tip_input = input("Suggested tip is 10%. To change it, type a new %, otherwise press ENTER: ")
    tip = float(tip_input) if tip_input.strip() else 10.0
    calc_tip(tip, bill)
except ValueError:
    print("Please enter a valid numeric tip or bill amount.")