prices = []
while True:
    price = float(input("Enter item price (0 to finish): "))
    if price == 0:
        break
    elif price > 0:
        prices.append(price)
    else:
        print("Invalid price. Try again.")
total = sum(prices)
number_of_items = len(prices)

if number_of_items > 0:
    average = total / number_of_items
else:
    average = 0
print("\n--- Checkout Summary ---")
print("Total purchase amount: $", total)
print("Number of items:", number_of_items)
print("Average item cost: $", average)
