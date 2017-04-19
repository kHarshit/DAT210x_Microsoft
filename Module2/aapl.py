import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# path = "https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv"
path = 'Datasets/AAPL_stock.csv'
df = pd.read_csv(path)
# print(df)

# close_arr = df['Close'].values
# close_arr2 = df['Close']
# close_arr2.plot()
df.plot()  # plot all series at once
# df.plot(subplots=True)
# plt.plot(df) # NOT working
# plt.plot(close_arr)
# plt.plot(close_arr2)
plt.title('AAPL stock')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.yscale('log')
# plt.axis('2017', 0)
df['Open'].plot(color='b', style='.-', legend=True)
df['Close'].plot(color='r', style='.', legend=True)
plt.show()
