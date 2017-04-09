import pandas as pd
import os

os.chdir("../Module1/")
cwd = os.getcwd()
print(cwd)

# TODO: Load up the 'tutorial.csv' dataset
csv_df = pd.read_csv('tutorial.csv', sep=',')

# TODO: Print the results of the .describe() method
print(csv_df)
print(csv_df.describe())
print(csv_df.info())
print(csv_df.head(3))  # csv_df.iloc[:3, :] OR tail(); default no is 5
print(csv_df.columns)  # display the name of the columns
print(csv_df.index)
print(csv_df.dtypes)  # what data type Pandas assigned each column


# TODO: Figure out which indexing method you need to use in order to index your dataframe with: [2:4,'col3']:
print(csv_df.loc[2:4, 'col3'])  # .ix uses hybrid approach of selecting by column label and column index

