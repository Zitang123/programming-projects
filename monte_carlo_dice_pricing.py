import random

simulations = int(input("Enter number of simulations: "))

winnings = []
counts = []

for _ in range(0, simulations):
    ended = False

    winning = 0
    count = 0
    while not ended:
        n = random.randint(1,6)
        count += 1
        if n <= 3:
            winnings.append(winning)
            counts.append(count)
            ended = True
        elif n == 6:
            winning += 5
        else:
            winning += 2

print(f"Average winnings: £{sum(winnings) / len(winnings):.2f}")
print(f"Maximum winnings: {max(winnings)}")
print(f"Games ending immediately: {100 * counts.count(1) / len(counts):.2f}%")
print(f"Average rolls per game: {sum(counts) / len(counts):.2f}")


