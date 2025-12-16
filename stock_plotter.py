import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

try:
    stock_symbol = input("Enter the stock's ticker symbol: ").strip().upper()
    if not stock_symbol:
        raise ValueError("Ticker symbol cannot be empty")

    print("1. Last 7 days\n2. Last 30 days\n3. Last 3 months\n4. Custom")
    choice = input("Choose: ").strip()

    if choice == '1':
        start_date = datetime.now() - timedelta(days=7)
    elif choice == '2':
        start_date = datetime.now() - timedelta(days=30)
    elif choice == '3':
        start_date = datetime.now() - timedelta(days=90)
    elif choice == '4':
        start_date = datetime.strptime(
            input("Start date (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        )
    else:
        raise ValueError("Invalid menu choice")

    end_date = datetime.now()

    stock_data = yf.download(
        stock_symbol,
        start=start_date.strftime('%Y-%m-%d'),
        end=end_date.strftime('%Y-%m-%d'),
        progress=False
    )

    if stock_data.empty:
        raise RuntimeError("No data found (invalid ticker or market closed)")

    print(stock_data)

    plt.figure(figsize=(10, 6))
    plt.plot(
        stock_data.index,
        stock_data['Close'],
        label=f'{stock_symbol} Closing Price',
        marker='.'
    )
    plt.title(f"{stock_symbol} Closing Price")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Updated: {datetime.now().strftime('%H:%M:%S')}")

except ValueError as e:
    print("Input Error:", e)

except RuntimeError as e:
    print("Data Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
