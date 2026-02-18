customers = {
    "Alice": 800,
    "Bob": 2000,
    "Carol": 6000,
    "David": 4500
}

bronze = 0
silver = 0
gold = 0

for customer in customers:
    total = customers[customer]

    if total < 1000:
        bronze += 1
    elif total < 5000:
        silver += 1
    else:
        gold += 1

print("\n--- Loyalty Tier Summary ---")
print("Bronze:", bronze)
print("Silver:", silver)
print("Gold:", gold)
