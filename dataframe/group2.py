import pandas as pd
df = pd.read_csv('GoogleApps.csv')

temp = df.pivot_table(index = 'Category', columns = 'Content Rating', values = 'Reviews', aggfunc = 'max')
print(temp)