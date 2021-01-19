import pandas as pd

census_incidents = pd.read_csv('incidentsNearDetails_with_tracts.csv', encoding='utf-8')
hoods_incidents = pd.read_csv('incidentsNearDetails_with_neighborhood.csv', encoding='utf-8')

summation = census_incidents.groupby(['GEOID10', 'OFFENSE_DESCRIPTION']).size().reset_index(name='COUNT')
summation_hood = hoods_incidents.groupby(['Neighborho', 'Name', 'OFFENSE_DESCRIPTION']).size().reset_index(name='COUNT')


summation.to_csv('incidentsNearDetails_tractSummation.csv', encoding='utf-8')
summation_hood.to_csv('incidentsNearDetails_neighborhoodSummation.csv', encoding='utf-8')

incidents = pd.read_csv('incidentsNearDetails_neighborhoodSummation.csv', encoding='utf-8')


incidents['Neighborho'] = incidents['Neighborho'].astype(int)
nid = incidents['Neighborho'].tolist()
unique_nid = list(set(nid))

df_list = {}

for i in unique_nid:
    df_list[i] = incidents[incidents.Neighborho==i]

t_df = df_list[2].transpose()
t_df.to_csv('incidentsGroupedSumNeighborhoodID-test.csv', encoding='utf-8')

