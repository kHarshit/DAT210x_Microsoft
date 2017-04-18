import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Datasets/SN_d_tot_V2.0.csv')
# print(df)

""" CSV file doesn't have column labels
Column 1-3: Gregorian calendar date
Column 4: Date in fraction of year
Column 5: Daily total sunspot number. A value of -1 indicates that no number is available for that day (missing value).
Column 6: Daily standard deviation of the input sunspot numbers from individual stations.
Column 7: Number of observations used to compute the daily value.
Column 8: Definitive/provisional indicator."""
file_path = 'Datasets/SN_d_tot_V2.0.csv'
col_names = ['year', 'month', 'day', 'dec_date', 'sunspots/day', 'std_dev', 'no_of_obs', 'indicator']
sunspots = pd.read_csv(file_path, sep=';', header=None, names=col_names, na_values={'std_dev': [' -1']}, parse_dates=[[0, 1, 2]])
# to prevent pandas from assuming first line of column gives header labels.
print(sunspots.iloc[10:20, :])
# print(sunspots.info())
# sunspots.to_csv('sunspots.csv', sep='\t')  # .to_excel()

