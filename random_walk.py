import random

current = int(input("Current value: "))

num = int(input("Number of simulations: "))

for i in range(0, num):
    n = random.randint(0,1)
    if n == 0:
        current += 1
    else:
        current -= 1

print(current)