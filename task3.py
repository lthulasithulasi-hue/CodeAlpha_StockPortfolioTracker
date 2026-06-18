


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 200
}

print("===== STOCK PORTFOLIO TRACKER =====")

portfolio = {}
total_investment = 0


num_stocks = int(input("How many different stocks do you own? "))

for i in range(num_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found in price list!")

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(f"{stock}: {quantity} shares × ${price} = ${value}")

print(f"\nTotal Portfolio Value = ${total_investment}")


with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock}: {quantity} shares × ${price} = ${value}\n"
        )

    file.write(f"\nTotal Portfolio Value = ${total_investment}")

print("\nPortfolio report saved as 'portfolio_report.txt'")