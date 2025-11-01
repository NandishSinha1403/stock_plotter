import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


stock_symbol  = input("Enter the stock's ticker symbol : ")


print("1. Last 7 days\n2. Last 30 days\n3. Last 3 months\n4. Custom")
choice = input("Choose: ")

if choice == '1':
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
elif choice == '2':
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
elif choice == '3':
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
else:
    start_date = input("Start date (YYYY-MM-DD): ")

end_date = datetime.now().strftime('%Y-%m-%d')

stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

print(stock_data)
plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data['Close'], label=f'{stock_symbol} Closing Price', color='blue',marker = '.')
plt.title(f"{stock_symbol} Closing Price ")
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
print(f"Updated: {datetime.now().strftime('%H:%M:%S')}")
