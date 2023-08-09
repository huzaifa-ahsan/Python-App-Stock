import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Set Streamlit app title
st.title('Stock Price Chart App')

# Create input widgets for stock symbol and time duration
stock_symbol = st.text_input('Enter stock symbol (e.g., AAPL)', value='AAPL')
start_date = st.date_input('Select start date', value=datetime.date(2020, 1, 1))
end_date = st.date_input('Select end date', value=datetime.date.today())

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display stock data
st.write(f"Displaying data for {stock_symbol}")
st.write(stock_data)

# Plot stock price chart
st.write("Stock Price Chart")
st.line_chart(stock_data['Close'])
