import random

fair_value = int(input("Enter fair value: "))
half_spread = int(input("Enter half-spread: "))
number_of_trades = int(input("Enter number of trades: "))

bid = fair_value - 2 * half_spread
ask = fair_value + 2 * half_spread

cash = 0
inventory = 0

max_inventory = inventory
min_inventory = inventory

print(f"Quote: {bid}|{ask}")

for _ in range(0, number_of_trades):

    trade = random.randint(0, 1)

    if trade == 0:
        cash += ask
        inventory -= 1
    elif trade == 1:
        cash -= bid
        inventory += 1

    max_inventory = max(max_inventory, inventory)
    min_inventory = min(min_inventory, inventory)

PnL = cash + inventory * fair_value

print(f"Final cash: {cash}")
print(f"Final inventory: {inventory}")
print(f"Final PnL: {PnL}")
print(f"Maximum inventory: {max_inventory}")
print(f"Minimum inventory: {min_inventory}")