expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0

print("\n--- Expense Summary ---")

for category in expenses:
    category_total = 0
    
    for amount in expenses[category]:
        category_total += amount
    
    print(category + " total: $", category_total)
    grand_total += category_total

print("Grand Total: $", grand_total)
