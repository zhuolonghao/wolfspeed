import datetime as dt
import pandas as pd
import yfinance as yf

symbol = "WOLF"

def process_expiration(exp_td_str):
    """
    Download Yahoo Finance call and put option quotes
    for a single expiration
    Input:
    exp_td_str = expiration date string "%Y-$m-$d"
        (a single item from yfinance.Ticker.options tuple)
    Return pandas.DataFrame with merged calls and puts data
    """

    options = tk.option_chain(exp_td_str)

    calls = options.calls
    puts = options.puts

    # Add optionType column
    calls['optionType'] = 'C'
    puts['optionType'] = 'P'

    # Merge calls and puts into a single dataframe
    exp_data = pd.concat(objs=[calls, puts], ignore_index=True)

    return exp_data


tk = yf.Ticker(symbol)
expirations = tk.options

# Create empty DataFrame, then add individual expiration data to it
data = pd.DataFrame()

for exp_td_str in expirations:
    exp_data = process_expiration(exp_td_str)
    data = pd.concat(objs=[data, exp_data], ignore_index=True)

# Add underlyingSymbol column
data['underlyingSymbol'] = symbol
data.to_excel('option_chain.xlsx')