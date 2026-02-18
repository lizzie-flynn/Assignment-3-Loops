sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}

def calculate_commission(amount):
    return amount * 0.10

print("\n--- Commission Leaderboard ---")

for person in sales:
    commission = calculate_commission(sales[person])
    print(person, "earned $", commission)
