import pandas as pd
import csv

df = pd.read_csv('Detail_Records_January_to_December_2019.csv', encoding='utf-8')

df['Street_No'] = df['Street_No'].fillna('')
df['Street_No'] = df['Street_No'].astype(str)
df['Street_No'] = df['Street_No'].str.rstrip('.0')
df['address'] = df['Street_No'] + " " + df['Street'].fillna('') + " AND " + df['xStreet'].fillna('')
df['address'] = df['address'].str.rstrip(' AND ')
df['address'] = df['address'].str.strip()

addresses = df['address'].tolist()

unique_addresses = set(addresses)
unique_addresses = list(unique_addresses)

df.to_csv('output_with_addresses.csv', encoding='utf-8')

csv_file = 'unique_addresses.csv'
names = ['Address']

with open(csv_file, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(unique_addresses)
