# Simple Stock Portfolio Tracker

# Hardcoded dictionary containing stock prices
stock_prices = {
    "TCS": 2300,
    "INFY": 1000,
    "RELIANCE": 1800,
    "HDFCBANK": 700,
    "WIPRO": 500
}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- ₹", price)

# User input
stock_name = input("\nEnter Stock Name: ").upper()

# Check if stock exists
if stock_name in stock_prices:
    quantity = int(input("Enter Quantity: "))

    # Calculate investment
    price = stock_prices[stock_name]
    total_investment = quantity * price

    # Display result
    print("\n----- Investment Details -----")
    print("Stock Name      :", stock_name)
    print("Price per Share : ₹", price)
    print("Quantity        :", quantity)
    print("Total Investment: ₹", total_investment)

    # Save result to a text file
    file = open("portfolio.txt", "w")
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("-------------------------\n")
    file.write(f"Stock Name : {stock_name}\n")
    file.write(f"Price      : ₹{price}\n")
    file.write(f"Quantity   : {quantity}\n")
    file.write(f"Total Value: ₹{total_investment}\n")
    file.close()

    print("\nPortfolio saved successfully in 'sumit.txt'.")

else:
    print("\n error:-Stock not available in the 'sumit.txt'.")