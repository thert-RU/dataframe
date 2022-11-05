import pandas as pd
df = pd.read_csv('GoogleApps.csv')

temp = df.groupby(by = 'Type')['Rating'].agg(['min', 'mean', 'max'])
print(round(temp, 1))