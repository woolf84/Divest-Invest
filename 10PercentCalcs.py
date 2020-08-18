import pandas as pd
import csv

df = pd.read_csv('EarningsSummation2019.csv', encoding='utf-8')

def SalaryStat(df, name):
    dept = df.loc[df['DEPARTMENT_NAME'] == name]
    dept_10 = dept.loc[dept['MoreThan10'] == True]
    if dept_10.empty:
        stats = {'DEPARTMENT_NAME' : name,
                 'max': 0,
                'median': 0,
                'mean': 0,
                'min': 0
                 }
    else:
        salaries = pd.to_numeric(dept_10['AnnualSalary'])
        stats = {'DEPARTMENT_NAME' : name,
                 'max' : salaries.max(),
                 'median' : salaries.median(),
                 'mean': salaries.mean(),
                 'min': salaries.min()
                 }
    return stats

stats_list = []

for i in df.DEPARTMENT_NAME.unique():
    stats_list.append(SalaryStat(df, i))

c_names = stats_list[0].keys()
csv_file = '10-percent-stats.csv'

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=c_names)
    writer.writeheader()
    for i in stats_list:
        writer.writerow(i)

