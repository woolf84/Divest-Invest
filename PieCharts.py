import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Histos_Percents.csv', encoding='utf-8')

df['0_90K']=df.iloc[:,2:11].sum(axis=1)
df['120K_']=df.iloc[:,14:27].sum(axis=1)
df['0_120K']=df.iloc[:,2:15].sum(axis=1)
df['140K_']=df.iloc[:,16:27].sum(axis=1)
df['0_40K']=df.iloc[:,2:6].sum(axis=1)
df['70K_']=df.iloc[:,9:27].sum(axis=1)
df['0_50K']=df.iloc[:,2:7].sum(axis=1)
df['60K_']=df.iloc[:,8:27].sum(axis=1)

bpd = 'Boston Police Department'
bfd = 'Boston Fire Department'
pwd = 'Public Works Department'
bps = 'BPS Facility Management'
parks = 'Parks Department'

BPD_df = df.loc[df['DEPARTMENT_NAME'] == bpd]
BPD_val_df = BPD_df.loc[:, ['0_90K','90_100K', '100_110K','110_120K','120K_']]
BFD_df = df.loc[df['DEPARTMENT_NAME'] == bfd]
BFD_val_df = BFD_df.loc[:, ['0_120K','120_130K', '130_140K','140K_']]
PWD_df = df.loc[df['DEPARTMENT_NAME'] == pwd]
PWD_val_df = PWD_df.loc[:, ['0_40K','40_50K', '50_60K','60_70K','70K_']]
BPS_df = df.loc[df['DEPARTMENT_NAME'] == bps]
BPS_val_df = BPS_df.loc[:, ['0_50K','50_60K','60_70K','70_80K','80_90K']]
Parks_df = df.loc[df['DEPARTMENT_NAME'] == parks]
Parks_val_df = Parks_df.loc[:, ['0_40K','40_50K', '50_60K','60K_']]

BPD_val_list = BPD_val_df.to_numpy().tolist()
BPD_val_list = BPD_val_list[0]

BPD_labels = '0 to 90K', '90-100K', '100-110K','110-120K', '120K and up'
BFD_labels = '0 to 120K', '120-130K', '130-140K','140K and up'
PWD_labels = '0 to 40K', '40-50K', '50-60K','60-70K','70K and up'
BPS_labels = '0 to 50K', '50-60K','60-70K','70-80K', '80K and up'
Parks_labels = '0 to 40K', '40-50K', '50-60K','60K and up'


#plt.pie(BPD_val_list,labels=BPD_labels,autopct='%100.1f%%', )
#ax.legend().draggable()
#fig, ax1 = plt.subplots(figsize = (12,12))
#ax1.pie(BPD_val_list,autopct='%100.1f%%',pctdistance=.5, labeldistance=.5,textprops={'fontsize': 14},center=(6,0))
#ax1.legend(BPD_labels,loc="upper right")
#plt.title("Breakdown of Annual Salary for BPD Employees Making more than 10% of in Overtime")
#plt.tight_layout()
#plt.show()
