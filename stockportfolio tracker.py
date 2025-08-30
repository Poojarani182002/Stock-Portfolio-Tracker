import yfinance as yf

# Your Portfolio: Ticker, Quantity, Buy Price
portfolio = [
    {"ticker": "AAPL", "quantity": 10, "buy_price": 150},
    {"ticker": "TSLA", "quantity": 5, "buy_price": 700},
]

total_investment = 0
total_current = 0

for stock in portfolio:
    ticker = stock["ticker"]
    qty = stock["quantity"]
    buy_price = stock["buy_price"]

    # Get current stock price
    current_price = yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1]

    # Calculate values
    investment = qty * buy_price
    current_value = qty * current_price
    profit_loss = current_value - investment

    # Add to totals
    total_investment += investment
    total_current += current_value

    # Print stock result
    print(f"\n{ticker}:")
    print(f"  Quantity: {qty}")
    print(f"  Buy Price: ${buy_price}")
    print(f"  Current Price: ${current_price:.2f}")
    print(f"  Investment: ${investment:.2f}")
    print(f"  Current Value: ${current_value:.2f}")
    print(f"  Profit/Loss: ${profit_loss:.2f}")

# Print total portfolio result
print("\n----- Portfolio Summary -----")
print(f"Total Investment: ${total_investment:.2f}")
print(f"Current Value: ${total_current:.2f}")
print(f"Overall Profit/Loss: ${total_current - total_investment:.2f}")
