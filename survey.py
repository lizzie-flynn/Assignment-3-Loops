preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

for item in preferences:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

total = len(preferences)

print("\n--- Market Share ---")
for product in counts:
    percentage = (counts[product] / total) * 100
    print(product + ":", round(percentage, 2), "%")
