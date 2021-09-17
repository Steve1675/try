# Define a main function that prints "Greetings!" to the console
def main():
    print("Greetings!")

explain before calling!
what is calling?

# %%

# Define a main function that accepts a string argument
def main(stock_ticker):
    print(stock_ticker + " is booming right now!")

what are inputs?

# %%

# Define a calculate_market_cap function that returns an integer
def calculate_market_cap(market_price, number_of_shares):
    cap = market_price * number_of_shares

    return cap

keep going

# %%

stock_ticker = "SBUX"
market_price = 76.06
number_of_shares = 1243600000

# %%

market_cap = calculate_market_cap(market_price, number_of_shares)
print(f"{stock_ticker} Market Capitalization: {market_cap}")
print(f"Data type of market_cap variable is: {type(market_cap)}")

# %%

mention local (cap) vs global variables

# Capture function output and print output value and data type
def calculate_market_cap(market_price, number_of_shares):

    # local var
    cap = market_price * number_of_shares

    return cap

# global vars
market_price = 76.06
number_of_shares = 1243600000

# %%

market_cap = calculate_market_cap(market_price, number_of_shares)
print(f"Market Capitalization: {market_cap}")
print(f"Data type of market_cap variable is: {type(market_cap)}")

# %%


