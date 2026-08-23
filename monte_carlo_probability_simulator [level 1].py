import random

number_of_dice = int(input("How many dice: "))
target_sum = int(input("Target sum: "))
simulations = int(input("Number of simulations: "))


sums = []


for i in range(simulations):
    sum_of_dice = 0
    for j in range(number_of_dice):
        num = random.randint(1, 6)
        sum_of_dice += num
    sums.append(sum_of_dice)

count = 0
for num in sums:
    if num >= target_sum:
        count += 1

print(f"The estimated probability if P(sum >= {target_sum}) is {count/simulations}")