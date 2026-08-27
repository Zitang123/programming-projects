import random

current = int(input("Current value: "))

num = int(input("Number of simulations: "))

states = []

for i in range(0, num):
    n = random.randint(0,1)
    if n == 0:
        current += 1
    else:
        current -= 1
    
    states.append(current)

max_count = 0
for state in states:
    max_count = max(max_count, states.count(state))

print(current)
print(f"Most landed on state: {max_count}")