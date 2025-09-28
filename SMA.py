import yfinance as yf  # type: ignore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#step 1 :- FETCHING DATA
ticker = 'RELIANCE.NS'
data = yf.download (ticker, period = '1y', interval = '1d')

#step 2 :- CALCULATING SMA
short_window = 50
long_window = 200

# Calculate the simple Moving Averages (SMA)
data['SMA_short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
data['SMA_long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

#step 3 :- GENERATING SIGNALS
data['Signal'] = 0.0
data.loc[data['SMA_short'] > data['SMA_long'], 'Signal'] = data.loc[data['SMA_short'] < data['SMA_long'], 'Signal'] = -1
data.loc[data['SMA_short'] < data['SMA_long'], 'Signal'] = -1
data['Position'] = data['Signal'].diff()


# STEP 5 :- VISUALIZATION
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.6)
plt.plot(data['SMA_short'], label=f'{short_window}-Day SMA', color='green', linestyle='--')
plt.plot(data['SMA_long'], label=f'{long_window}-Day SMA', color='red', linestyle='--')


# Plot the Buy signals 
plt.plot(data[data['Position'] == 2].index, 
         data['SMA_short'][data['Position'] == 2],
         '^', markersize=12, color='green', lw=0, label='BUY Signal')

# Plot the Sell signals 
plt.plot(data[data['Position'] == -2].index, 
         data['SMA_short'][data['Position'] == -2],
         'v', markersize=12, color='red', lw=0, label='SELL Signal')


#  Chart Formatting 
plt.title(f'{ticker} - SMA Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

print("Script finished.")
