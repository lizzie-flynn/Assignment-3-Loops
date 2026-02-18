revenues = [3, 5, 8]

print("\n--- Revenue Chart ---")

for i in range(len(revenues)):
    bars = "#" * revenues[i]
    print("Year", i + 1, ":", bars)
