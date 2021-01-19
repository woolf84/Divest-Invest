import pandas as pd

census_details = pd.read_csv('Details_2019_C_Latlng_Chunks/Details_Census_Tracts_Joined.csv', encoding='utf-8')
census_tracts = pd.read_csv('Details_2019_C_Latlng_Chunks/Details_C_CensusTracts_Counts.csv', encoding='utf-8')

summation = census_details.groupby(['GEOID10'])['Pay_Amount','Minutes_Worked','Pay_Hours'].sum()

df_merge = pd.merge(census_tracts,summation,on='GEOID10', how='left')

df_merge.to_csv('Details_2019_C_Latlng_Chunks/Details_C_CensusTracts_Counts_Sums.csv', encoding='utf-8')
