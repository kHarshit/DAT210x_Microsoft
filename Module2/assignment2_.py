import pandas as pd

# TODO: Load up the dataset Ensuring you set the appropriate header column names

df = pd.read_csv('Datasets/direct_marketing.csv')
print(df)

# print(df.recency)  # produces a series object
# print(df['recency'])  # produces a dataframe
"""By using the column name in the code, it's very easy to discern what is being pulled, and you don't have to worry
about the order of the columns. Doing this lookup of first matching the column name before slicing the column index
is marginally slower than directly accessing the column by index."""
# print(df[['recency']])
# print(df.loc[:, 'recency'])  # selects by column label
# print(df.loc[:, ['recency']])
"""By passing in a list of parameters, you can select more than one column to slice. If you use this syntax, even if
you only specify a single column, the data type that you'll get back is a dataframe as opposed to a series"""
print(df.iloc[:, 0])  # selects by column index
# print(df.iloc[-5:, :])
# print(df.iloc[:, [0]])
# print(df.ix[:, 0])  # to use hybrid approach of either
"""Note that .loc[] and .ix[] are inclusive of the range of values selected, where .iloc[] is non-inclusive. In that
sense, df.loc[0:1, :] would select the first two rows, but only the first row would be returned using df.iloc[0:1, :]."""

# print(df.recency < 7)
# print(df[(df.recency < 7) & (df.newbie == 0)])
