import pandas as pd
df = pd.read_csv('GoogleApps.csv')

temp = df['Category'].value_counts()
print('кол-во приложений из категории "BUSINESS": ',temp['BUSINESS'])

temp = df['Content Rating'].value_counts()
ratio = (temp['Teen'] / temp['Everyone 10+']).round(2)
print('соотношение количества приложений Teen / Everyone10+: ',ratio)

temp = df.groupby(by = 'Type')['Rating'].mean()

print('Средний рейтинг платных приложений: ',temp['Paid'])
print('разница средних рейтингов платных и бесплатных приложений: ', round(temp['Paid'] - temp['Free'], 2))

temp = df.groupby(by = 'Category')['Size'].agg(['min', 'max'])
print(temp.loc['COMICS'])

