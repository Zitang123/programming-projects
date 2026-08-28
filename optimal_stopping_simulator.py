import random

T = int(input("Enter threshhold between 1 and 100: "))
max_rolls = int(input("Maximum number of rolls: "))

count = 0
final = 0

while count < max_rolls:
    num = random.randint(1, 100)
    count += 1

    if count == max_rolls:
        print(f"Roll {count}: {num} - Forced stop")
        final = num
        break

    if num >= T:
        print(f"Roll {count}: {num} - Stop")
        final = num
        break

    print(f"Roll {count}: {num} - Continue")

print(f"Final Score: {final}")
print(f"Rolls: {count}")