import random

starting_value = int(input("Enter starting value: "))
half_spread = int(input("Enter half-spread: "))
trades = int(input("Enter number of trades: "))

cash = 0
inventory = 0
fair_value = starting_value

inventories = []

for _ in range(0, trades):

    inventories.append(inventory)

    bid = fair_value - half_spread
    ask = fair_value + half_spread

    n = random.randint(0, 1)

    if n == 0:
        new_fair_value = fair_value + 1
    else:
        new_fair_value = fair_value - 1

    if new_fair_value > fair_value:
        cash += ask
        inventory -= 1
    else:
        cash -= bid
        inventory += 1

    fair_value = new_fair_value

inventories.append(inventory)

PnL = cash + inventory * fair_value

print(f"Final fair value: {fair_value}")
print(f"Final cash: £{cash:.2f}")
print(f"Final inventory: {inventory}")
print(f"Final PnL: £{PnL:.2f}")
print(f"Maximum inventory: {max(inventories)}")
print(f"Minimum inventory: {min(inventories)}")