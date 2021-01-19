import pandas as pd

details = pd.read_csv('Details_2019_C.csv', encoding='utf-8')

subset_df = details[['Customer_No', 'Customer_Name', 'Street', 'Start_date']]
subset_df = subset_df.drop_duplicates()

subset_df.to_csv('unique_details_C.csv', index=False, encoding='utf-8')