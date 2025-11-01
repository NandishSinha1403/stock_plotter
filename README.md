
# Stock Price Visualizer

This project allows users to retrieve and visualize historical stock price data using a ticker symbol. It leverages the [Yahoo Finance](https://finance.yahoo.com) API via the `yfinance` Python library and plots the closing prices using `matplotlib`.

---

## Features

- Fetch stock data from **Yahoo Finance**
- Supports multiple time ranges:
  - Last 7 days
  - Last 30 days
  - Last 3 months
  - Custom date range
- Interactive command-line input
- Line chart of closing prices with date and price axes
- Displays timestamp of last update

---

## Requirements

Make sure you have the following Python libraries installed:

```bash
pip install yfinance matplotlib
```

---

## How to Use

1. Run the script:
   ```bash
   python stock_plotter.py
   ```

2. Enter a valid ticker symbol (e.g., `AAPL`, `TSLA`, `RELIANCE.NS`).

3. Choose a time range:
   ```
   1. Last 7 days
   2. Last 30 days
   3. Last 3 months
   4. Custom
   ```

4. If you choose "Custom", enter a start date in `YYYY-MM-DD` format.

5. The script will fetch and display the stock data, and plot the closing prices.

---

## Supported Exchanges

You can use ticker symbols from various global exchanges by appending the correct suffix:

| Exchange         | Suffix     | Example         |
|------------------|------------|------------------|
| NASDAQ (USA)     | *(none)*   | `AAPL`           |
| NYSE (USA)       | *(none)*   | `IBM`            |
| NSE (India)      | `.NS`      | `RELIANCE.NS`    |
| BSE (India)      | `.BO`      | `TCS.BO`         |
| London (UK)      | `.L`       | `HSBA.L`         |
| Toronto (Canada) | `.TO`      | `RY.TO`          |
| Tokyo (Japan)    | `.T`       | `7203.T`         |

🔗 [TICKER LOOKUP FROM YAHOO! FINANCE] : <a href = "https://finance.yahoo.com/lookup/">Yahoo! Finance Lookup</a>

---

## Sample Output

- A line chart showing the stock’s closing price over the selected time range.

![BTC_USD.png](attachment:BTC_USD.png)

- Console output of the raw data table.

![image.png](attachment:image.png)

---

