import yfinance as yf

def fetch_stock_data():
    # Prompt the user for input
    ticker_symbol = input("Enter the stock ticker symbol: ").upper()
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Fetch the stock data
    stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # Check if data was fetched successfully
    if stock_data.empty:
        print(f"No data found for ticker symbol '{ticker_symbol}' between {start_date} and {end_date}.")
        return

    # Print the opening and closing prices
    print(f"\nStock data for {ticker_symbol} from {start_date} to {end_date}:")
    print(stock_data[['Open', 'Close']])

# Run the function
fetch_stock_data()
