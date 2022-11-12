import pandas as pd
from data_cleaning import *

# Очистка данных из первого задания

# Замени тип данных на дробное число (float) для цен приложений ('Price')
print(df[df['Type'] == 'Paid']['Price'].head(5))
def set_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0

df['Price'] = df['Price'].apply(set_price)
print(df[df['Type'] == 'Paid']['Price'].head(5))
# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
def set_installs(installs):
    if installs[-1] == '+':
        installs = installs[:-1]
    installs = installs.replace(',', '')
    return int(installs)

df['Installs'] = df['Installs'].apply(set_installs)

df['Profit'] = df['Installs'] * df['Price']

print(df[df['Type'] == 'Paid']['Profit'].head(5))

# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?

# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'

# Какое максимальное количество жанров ('Number of genres') хранится в датасете?

# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'

# Выведи на экран сезоны и их количество в датасете