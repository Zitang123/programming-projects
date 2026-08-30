import random

stock_price = int(input("Starting stock price: "))
strike_price = int(input("Strike price: "))
simulations = int(input("Number of simulations :"))

options = []
final_stocks = []

for _ in range(0, simulations):
    n = random.randint(-40, 40)

    final_price = stock_price + n
    final_stocks.append(final_price)
    option = max(final_price - strike_price, 0)

    options.append(option)

count = 0
for option in options:
    if option >0:
        count += 1


print(f"Average payoff: £{sum(options)/len(options):.2f}")
print(f"Probability of profit {100 * count/len(options):.2f}%")
print(f"Maximum payoff: £{max(options):.2f}")
print(f"Average final stock price: £{sum(final_stocks)/len(final_stocks):.2f}")