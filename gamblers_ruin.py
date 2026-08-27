import random

bankrupt = 0
reached = 0

for _ in range(0, 10000):
    starting = 50
    target = 100

    count = 0

    while starting != 100 and starting != 0:
        n = random.randint(0,1)

        if n == 0:
            starting += 1
        else:
            starting -= 1

        count += 1

    if starting == 0:
        bankrupt += 1
    else:
        reached += 1

print(f"Bankrupt: {bankrupt}")
print(f"Reached: {reached}")