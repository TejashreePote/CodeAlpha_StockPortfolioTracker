# Stock Portfolio Tracker
import csv 
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ₹{price}")

while True:

    stock = input("\nEnter stock symbol: ").upper()

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append({
            "stock": stock,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"\n{stock} added successfully!")
        print(f"Investment: ₹{investment}")

    else:
        print("Stock not available.")

    choice = input("\nDo you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break


# Display Portfolio

print("\n====================================")
print("          YOUR PORTFOLIO")
print("====================================")

total_investment = 0

for item in portfolio:
    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ₹{item['price']} | "
        f"Investment: ₹{item['investment']}"
    )

    total_investment += item["investment"]

print("------------------------------------")
print(f"Total Investment: ₹{total_investment}")
print("====================================")

# Save portfolio to CSV
with open("portfolio.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock","Quantity","Price","Investment"])

    for item in portfolio:
        writer.writerow([
            item["stock"],
            item["quantity"],
            item["price"],
            item["investment"]
        ])

print("\nPortfolio saved to portfolio.csv")