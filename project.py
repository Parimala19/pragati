# Import required libraries
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Download historical stock data for Tesla
tesla_data = yf.download('TSLA', start='2010-06-29', end='2023-12-31')
tesla_data.reset_index(inplace=True)

# Read Tesla revenue data from CSV
tesla_revenue = pd.read_csv("Tesla_Quarterly_Revenue.csv")
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(r"\$", "").str.replace(",", "")
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue["Revenue"] = pd.to_numeric(tesla_revenue["Revenue"])
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])

# Plot Tesla stock data
fig_tesla = go.Figure()
fig_tesla.add_trace(go.Scatter(x=tesla_data['Date'], y=tesla_data['Close'], name="TSLA Close"))
fig_tesla.update_layout(title="Tesla Stock Price", xaxis_title="Date", yaxis_title="Close Price (USD)")
fig_tesla.show()

# Download historical stock data for GameStop
gme_data = yf.download('GME', start='2010-06-29', end='2023-12-31')
gme_data.reset_index(inplace=True)

# Read GameStop revenue data from CSV
gme_revenue = pd.read_csv("GameStop_Quarterly_Revenue.csv")
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(r"\$", "").str.replace(",", "")
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
gme_revenue["Revenue"] = pd.to_numeric(gme_revenue["Revenue"])
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])

# Plot GameStop stock data
fig_gme = go.Figure()
fig_gme.add_trace(go.Scatter(x=gme_data['Date'], y=gme_data['Close'], name="GME Close"))
fig_gme.update_layout(title="GameStop Stock Price", xaxis_title="Date", yaxis_title="Close Price (USD)")
fig_gme.show()
