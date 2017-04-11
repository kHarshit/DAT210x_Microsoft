import pandas as pd

# TODO: Load up the dataset Ensuring you set the appropriate header column names
df = pd.read_csv('Datasets/servo.data')
df.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']

print(df.describe())

# TODO: Create a slice that contains all entries having a vgain equal to 5. Then print the length of(# of samples in) that slice:
k = df[df.iloc[:, 3] == 5]
print(k.describe())
print(len(k))


# TODO: Create a slice that contains all entries having a motor equal to E and screw equal
# to E. Then print the length of (# of samples in) that slice:
print(df[(df.iloc[:, 0] == 'E') & (df.iloc[:, 1] == 'E')])
l = df[(df['motor'] == 'E') & (df['screw'] == 'E')]
print(l.describe())
print(len(l))  # the answer should be 6; checkout read_csv() api documentation that will fix your issue!


# TODO: Create a slice that contains all entries having a pgain equal to 4. Use one of the various methods of finding
# the mean vgain value for the samples in that slice. Once you've found it, print it:
m = df[df.pgain == 4]
print(m.mean())
print(m.vgain.mean())


# TODO: (Bonus) See what happens when you run the .dtypes method on your dataframe!
print(df.dtypes)


