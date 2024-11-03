# stocks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('enter-stock-data/', views.show_stock_data, name='enter_stock_data'),
]
