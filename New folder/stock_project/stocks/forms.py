# stocks/forms.py
from django import forms

class StockDataForm(forms.Form):
    ticker_symbol = forms.CharField(label='Ticker Symbol', max_length=10)
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date'}))
