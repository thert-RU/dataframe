#место для твоего кода
import pandas as pd
df = pd.read_csv('investments_VC.csv')
df.info()
print(df[''].head(50))

temp = df[pd.isnull(df['name'])]
# def get_name(link):
#     if pd.isnull(link):
#         return link[14:].replace('-', ' ')
#     else:

# temp['name'] = temp['permalink'].apply(get_name)
# print(temp)
# df.info()
# df['name'] =
def fill_name(row):
    if pd.isnull(row['name']):
        row['name'] = row['permalink'][14:].replace('-', ' ')
    return row

df = df.apply(fill_name, axis=1)
df.info()