# trading-strategies-python
This project constitutes a quantitative analysis tool for Indian stocks that shows trading signals from a Simple Moving Average (SMA) crossover strategy.

The script fetches historical stock price data by way of the `yfinance` library as it calculates the short-term (50-day) and long-term (200-day) SMAs plus it identifies crossover points.
- BUY Signal: The 200-day SMA is crossed by the 50-day SMA above it.
The 50-day SMA crossing under the 200-day SMA triggers a SELL Signal. That is a signal to indicate the time when one should sell.

`matplotlib` is what is used for the plotting of the results.

1. Clone the repository.
2. The packages that are required should be installed now.
```bash
First install yfinance then install pandas then install matplotlib.
```
3. Run the script:
```bash
python sma_crossover.py
```
