import yfinance as yf
stock_data=yf.Ticker("AMZN")
print(stock_data.info)