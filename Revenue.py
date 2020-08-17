import pandas as pd
import csv

#df = pd.read_csv('//Users/daveweimer/Desktop/BPNP/Divest-Invest/StateBudget/Revenue/2019-Rev.csv', encoding='utf-8')
df = df = pd.read_csv('//Users/daveweimer/Desktop/BPNP/Divest-Invest/StateBudget/ActualVsBudget/Budget_Actual_With_Other_Spending_Authorizationv3.csv', encoding='utf-8')

#sde_df = df.loc[df['cabinet_name'] == 'SHERIFF DEPARTMENTS']
#sources = sde_df['revenue_source_name'].unique()
#sde_df.to_csv('//Users/daveweimer/Desktop/BPNP/Divest-Invest/StateBudget/Revenue/2019-SDE-Rev.csv', encoding='utf-8')

sde_df = df.loc[df['Cabinet/Secretariat Name'] == 'SHERIFF DEPARTMENTS']
sde_df.to_csv('//Users/daveweimer/Desktop/BPNP/Divest-Invest/StateBudget/ActualVsBudget/SDE.csv', encoding='utf-8')



