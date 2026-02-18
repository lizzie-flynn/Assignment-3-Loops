warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]

total_inventory = {}

for warehouse in warehouses:
    for product in warehouse["inventory"]:
        quantity = warehouse["inventory"][product]

        if product in total_inventory:
            total_inventory[product] += quantity
        else:
            total_inventory[product] = quantity

print("\n--- Total Supply Chain Inventory ---")
for product in total_inventory:
    print(product + ":", total_inventory[product])
