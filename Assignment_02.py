import yfinance as yf #library to retrive financial data from Yahoo Finance
from prettytable import PrettyTable #library to create tables for better data presentation

table = PrettyTable()

table.field_names = ["Stock ID", "Highest Price", "Lowest Price", "Today's Price"] #column headers of the table

#list of stock symbols (stock ID's)
ticker_symbols = ["2222.SR","1182.SR", "1183.SR", "4081.SR", "1150.SR", "1120.SR", "1140.SR", "1020.SR", "2170.SR", "2290.SR", "2250.SR"]   

#loop through each stock symbol
for ticker_symbol in ticker_symbols:
    stock = yf.Ticker(ticker_symbol)

     #retrive historical data for the specified date range
    data = stock.history(start="2023-01-01", end="2023-12-29")

     #find the highest price from the "High" column of historical data
    highest_price =data['High'].max()

    #find the lowest price from the "Low" column of historical data
    lowest_price=data['Low'].min()

    #get the current price of the stock
    todays_price =stock.info['currentPrice']

   #add rows to the table with stock information
    table.add_row([ticker_symbol,  f"{highest_price:.2f}",  f"{lowest_price:.2f}", todays_price])
     
print(table)



