import pandas as pd

df_1 = pd.read_csv('fio_people.csv', encoding='utf-8')
df_2 = pd.read_csv('fio_contacts.csv', encoding='utf-8')

df_union = pd.merge(df_1, df_2, how='outer', on='fc_num', sort=False)

df_union.to_csv('fio_union.csv', encoding='utf-8')