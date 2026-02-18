initial_revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (%): "))

revenue = initial_revenue

print("\nYear | Revenue")
print("----------------")

for year in range(1, 11):
    print(year, " | $", round(revenue, 2))
    revenue = revenue * (1 + growth_rate / 100)
