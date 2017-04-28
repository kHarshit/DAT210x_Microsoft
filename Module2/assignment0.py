import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


s = pd.Series([1, 3, 5, np.nan, 8])
print(s)
print(s.index, s.values)


"""Creating DataFrame by passing numpy array"""
dates = pd.date_range('20170404', periods=6)
print(dates)
print(np.random.randn(6, 4))
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print(df[::-1])  # reverse dataframe
df.at[dates[0], 'A'] = 0  # setting value by label
df.iat[0, 1] = 0  # setting value by position
print(df)
print(df.T)  # transpose of dataframe
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))  # sorted by values of B
df[df > 0] = -df  # a where operation with setting
print(df)


"""Creating DataFrame by passing dictionary"""
data_dict = {
    'weekday': ['mon', 'tue', 'wed', 'thu'],
    'city': ['Austin', 'Dallas', 'LA', 'Boston'],
    'visitors': [123, 232, 334, 234],
}
print(pd.DataFrame(data_dict))


"""Creating DataFrame by passing list"""
cities = ['Austin', 'Dallas', 'LA', 'Boston']
weekdays = ['mon', 'tue', 'wed', 'thu']
visitors = [123, 232, 334, 234]
list_labels = ['city', 'visitors', 'weekday']
list_cols = [cities, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))
print(zipped)
data_dict2 = dict(zipped)
print(pd.DataFrame(data_dict2))


"""Creating DataFrame by passing a dict of objects that can be converted to series-like"""
df2 = pd.DataFrame({ 'A': 1.,
                     'B': pd.Timestamp(20160104),
                     'C': pd.Series(1, index=list(range(4)), dtype='float64'),
                     'D': np.array([3]*4, dtype='int64'),
                     'E': pd.Categorical(['test', 'train', 'test', 'testing']),
                     'F': 'same'})
print(df2)
print(df2.dtypes)
print(df2[df2['E'].isin(['test', 'train'])])  # isin return a boolean Series showing whether each element in the Series


"""Broadcasting"""
users = pd.DataFrame(data_dict)  # broadcasts to entire column
users['fees'] = 0
print(users)

heights = [59.0, 64.2, 52.0, 62.0, 56.8]
data_b = {'heights': heights, 'sex': 'M'}
results = pd.DataFrame(data_b)
print(results)
results.columns = ['height (in)', 'sex']  # change index and column labels
results.index = ['A', 'B', 'C', 'D', 'E']
print(results)

file_name = "http://www.ats.ucla.edu/stat/data/binary.csv"
df3 = pd.read_csv(file_name)
print(df3)

# # Read in the file: df1
# df1 = pd.read_csv('world_population.csv')
# # Create a list of the new column labels: new_labels
# new_labels = ['year', 'population']
# # Read in the file, specifying the header and names parameters: df2
# df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)
# # Print both the DataFrames
# print(df1)
# print(df2)
#
#
# # Read the raw file as-is: df1
# df1 = pd.read_csv(file_messy)
# # Print the output of df1.head()
# print(df1.head())
# # Read in the file with the correct parameters: df2
# df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')
# # Print the output of df2.head()
# print(df2.head())
# # Save the cleaned up DataFrame to a CSV file without the index
# df2.to_csv(file_clean, index=False)
# # Save the cleaned up DataFrame to an excel file without the index
# df2.to_excel('file_clean.xlsx', index=False)


