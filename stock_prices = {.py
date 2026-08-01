stock_prices = {
    "AAPL": 180.50,
    "TSLA": 240.75,
    "GOOGL": 140.25,
    "MSFT": 410.00,
    "AMZN": 175.00
}

def show_prices():
    print("\n--- Available Stock Prices ---")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")

def main():
    show_prices()
    portfolio = {}
    total_portfolio_value = 0.0

    print("\nEnter your stocks. Type 'done' when you finish.")
    
    while True:
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
        if symbol == 'DONE':
            break
        if symbol not in stock_prices:
            print("Stock price not found in system. Try another.")
            continue
            
        try:
            shares = float(input(f"Enter number of shares for {symbol}: "))
        except ValueError:
            print("Please enter a valid number for shares.")
            continue
            
        value = shares * stock_prices[symbol]
        portfolio[symbol] = {"shares": shares, "value": value}
        total_portfolio_value += value

    print("\n========== PORTFOLIO SUMMARY ==========")
    summary_lines = ["========== PORTFOLIO SUMMARY ==========\n"]
    
    for symbol, data in portfolio.items():
        line = f"Stock: {symbol} | Shares: {data['shares']} | Value: ${data['value']:.2f}\n"
        print(line.strip())
        summary_lines.append(line)
        
    total_line = f"\nTotal Investment Value: ${total_portfolio_value:.2f}\n"
    print(total_line)
    summary_lines.append(total_line)

    file_name = "portfolio_summary.txt"
    with open(file_name, "w") as file:
        file.writelines(summary_lines)
    print(f"Portfolio successfully saved to {file_name}!")

if __name__ == "__main__":
    main()
