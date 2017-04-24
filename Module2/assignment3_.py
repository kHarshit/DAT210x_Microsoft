import pandas as pd

ordered_satisfaction = ['Very unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction': ['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype('category', ordered=True, categories=ordered_satisfaction).cat.codes
print(df)

ani = ['Bird', 'Bird', 'Mammal', 'Fish', 'Amphibian', 'Reptile', 'Mammal']
df = pd.DataFrame({'vertebrates': ani})
df['vertebrates'] = df.vertebrates.astype('category').cat.codes
print(df)

df2 = pd.get_dummies(df, columns=['vertebrates'])
print(df2)
