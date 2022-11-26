#место для твоего кода
import pandas as pd
df = pd.read_csv('investments_VC.csv')
#df.info()

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
#df.info()


def rounds_count(row):
    a = 0
    if row['round_A'] > 0:
        a += 1
    if row['round_B'] > 0:
        a += 1
    if row['round_C'] > 0:
        a += 1
    if row['round_D'] > 0:
        a += 1
    if row['round_E'] > 0:
        a += 1
    if row['round_F'] > 0:
        a += 1
    if row['round_G'] > 0:
        a += 1
    if row['round_H'] > 0:
        a += 1
    return a

df['rounds_rating'] = df.apply(rounds_count, axis=1)
#df.info()

#print(df['rounds_rating'].head(50))

def set_status(row):
    if pd.isnull(row['status']):
        row['status'] = 'closed'
    return row

df = df.apply(set_status, axis=1)

def int_usd(row):
    return int(row.replace(',', ''))
    
df['funding_total_usd'] = df['funding_total_usd'].apply(int_usd)


for i in range(9):
    temp = df[
        (df['rounds_rating'] == i) &
        ((df['status'] == 'operating') |
        (df['status'] == 'acquired'))
    ]
    print(round(len(temp)/len(df[df['rounds_rating'] == i]), 2)*100, '-', len(temp), 'startups')
    print(temp['funding_total_usd'].mean(), 'средняя сумма инвестиций в долларах сша')
