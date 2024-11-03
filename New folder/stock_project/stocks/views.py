# stocks/views.py
from django.shortcuts import render
from .forms import StockDataForm
import yfinance as yf
import matplotlib.pyplot as plt
import io
import urllib, base64

def show_stock_data(request):
    stock_data = None
    error_message = None
    chart_url = None

    if request.method == 'POST':
        form = StockDataForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker_symbol']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Fetch stock data using yfinance
            try:
                stock = yf.download(ticker, start=start_date, end=end_date)
                if not stock.empty:
                    stock_data = stock.to_html()  # Convert DataFrame to HTML table
                    
                    # Plot Open and Close prices
                    plt.figure(figsize=(10, 5))
                    plt.plot(stock.index, stock['Open'], label='Open Price', color='blue')
                    plt.plot(stock.index, stock['Close'], label='Close Price', color='green')
                    plt.xlabel('Date')
                    plt.ylabel('Price')
                    plt.title(f'{ticker} Stock Open and Close Prices')
                    plt.legend()

                    # Save the plot to a BytesIO object
                    buffer = io.BytesIO()
                    plt.savefig(buffer, format='png')
                    buffer.seek(0)
                    image_png = buffer.getvalue()
                    buffer.close()
                    chart_url = 'data:image/png;base64,' + urllib.parse.quote(base64.b64encode(image_png))
                    
                    plt.close()  # Close the plot to free memory
                else:
                    error_message = f"No data found for {ticker} from {start_date} to {end_date}."
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
    else:
        form = StockDataForm()

    context = {
        'form': form,
        'stock_data': stock_data,
        'error_message': error_message,
        'chart_url': chart_url,
    }
    return render(request, 'stocks/stock_form.html', context)
