total = 0
while True:
    amount = float(input("Enter amount: "))
    total = total + amount
    again = input("Add another expense? (yes/no): ")
    if again == "no":
        break
print("Total Expense:",total)