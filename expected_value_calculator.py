num_of_dice = int(input("Enter number of dice to use: "))
win_money = int(input("Enter amount to win when rolling a 6: "))
lose_money = int(input("Enter amount to lose when rolling anything else: "))

ev = num_of_dice * ( (1/6) * win_money - (5/6) * lose_money )
print(f"Expected value = {ev}")