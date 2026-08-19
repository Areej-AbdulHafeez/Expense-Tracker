expenses = []
total = 0

while True:
    name = input("Enter expense name: ")
    expenses.append(name)
    amount = float(input("Enter amount: "))
    total = total + amount
    again = input("Add another expense? (yes/no): ")
    if again == "no":
        break
print("Your Expenses:")
for expense in expenses:
    print(expense)
print("Total Expense:", total)