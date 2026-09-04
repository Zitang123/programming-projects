import random

price = int(input("Enter price: "))
fair_value = int(input("Enter fair value: "))
steps = int(input("Enter number of steps: "))

cash = 0
inventory = 0

buys = 0
sells = 0

inventories = [0]

for _ in range(steps):
    n = random.choice([-2, -1, 1, 2])

    price += n

    if price <= fair_value - 5:
        cash -= price
        inventory += 1
        buys += 1
    elif price >= fair_value + 5:
        cash += price
        inventory -= 1
        sells += 1

    inventories.append(inventory)
    
print(f"Final price: {price}")
print(f"Final cash: {cash}")
print(f"Final inventory: {inventory}")
print(f"Final PnL: {cash + inventory * price}")

print(f"Number of buys: {buys}")
print(f"Number of sells: {sells}")

print(f"Maximum inventory: {max(inventories)}")
print(f"Minimum inventory: {min(inventories)}")