import pandas as pd

df_1 = pd.read_csv('Details_2019_C_Latlng_Chunks/Chunk1-output.csv', encoding='utf-8')
df_2 = pd.read_csv('Details_2019_C_Latlng_Chunks/Chunk2-output.csv', encoding='utf-8')
df_3 = pd.read_csv('Details_2019_C_Latlng_Chunks/Chunk3-output.csv', encoding='utf-8')
df_4 = pd.read_csv('Details_2019_C_Latlng_Chunks/Chunk4-output.csv', encoding='utf-8')
df_5 = pd.read_csv('Details_2019_C_Latlng_Chunks/Chunk5-output.csv', encoding='utf-8')

all_df = [df_1, df_2, df_3, df_4, df_5]

details_census = pd.concat(all_df)
#inc_true = inc[inc.['MATCH_TENTH_KM'] == 'TRUE']
#inc_true.to_csv('incidents-chunks/incidents_details_true.csv', encoding='utf-8')
details_census.to_csv('Details_2019_C_Latlng_Chunks/details_census_tracts.csv', encoding='utf-8')