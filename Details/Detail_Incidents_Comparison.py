import pandas as pd
import geopy.distance
from datetime import datetime

#takes two sets of lat/long returns true if the distance between the points is less than a given distance in km
def compare_distance(lat1, lon1, lat2, lon2, dist):
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)
    return(geopy.distance.distance(coord1, coord2).km <= dist)

df_det = pd.read_csv('Details_2019_C_latlng.csv', encoding='utf-8')
df_inc = pd.read_csv('incidents-chunks/2019incidents-batch5.csv', encoding='utf-8')

inc_occur = df_inc['OCCURRED_ON_DATE'].tolist()

df_inc[['DATE','TIME']] = df_inc['OCCURRED_ON_DATE'].str.split(expand=True)
df_inc[['YEAR', 'MONTH', 'DAY']] = df_inc['DATE'].str.split("-", expand=True)
df_inc[['HOUR','MIN']] = df_inc['TIME'].str.split(":", expand=True)

df_inc['YEAR'] = df_inc['YEAR'].astype(int)
df_inc['MONTH'] = df_inc['MONTH'].astype(int)
df_inc['DAY'] = df_inc['DAY'].astype(int)
df_inc['HOUR'] = df_inc['HOUR'].astype(int)
df_inc['MIN'] = df_inc['MIN'].astype(int)

inc_year = df_inc['YEAR'].tolist()
inc_mon = df_inc['MONTH'].tolist()
inc_day = df_inc['DAY'].tolist()
inc_hr = df_inc['HOUR'].tolist()
inc_min = df_inc['MIN'].tolist()
inc_dates = []

for y, m, d, h, i in zip(inc_year, inc_mon, inc_day, inc_hr, inc_min):
    inc_dates.append(datetime(year=y, month=m, day=d, hour=h, minute=i))

df_det[['SYEAR', 'SMONTH', 'SDAY']] = df_det['Start_date'].str.split("-", expand=True)

df_det['SYEAR'] = df_det['SYEAR'].astype(int)
df_det['SMONTH'] = df_det['SMONTH'].astype(int)
df_det['SDAY'] = df_det['SDAY'].astype(int)

det_startyear = df_det['SYEAR'].tolist()
det_startmon = df_det['SMONTH'].tolist()
det_startday = df_det['SDAY'].tolist()

df_det['Start_Time'] = df_det['Start_Time'].astype(int)
det_starttime = df_det['Start_Time'].tolist()

det_startdates = []

for y, m, d, t in zip(det_startyear, det_startmon, det_startday, det_starttime):
    if len(str(t)) <= 2:
        det_startdates.append(datetime(year=y, month=m, day=d, hour=0, minute=t))
    else:
        if len(str(t)) <= 3:
            det_startdates.append(datetime(year=y, month=m, day=d, hour=int(str(t)[0]), minute=int(str(t)[1:])))
        else:
            det_startdates.append(datetime(year=y, month=m, day=d, hour=int(str(t)[:2]), minute=int(str(t)[2:])))

df_det[['EYEAR', 'EMONTH', 'EDAY']] = df_det['End_date'].str.split("-", expand=True)

df_det['EYEAR'] = df_det['EYEAR'].astype(int)
df_det['EMONTH'] = df_det['EMONTH'].astype(int)
df_det['EDAY'] = df_det['EDAY'].astype(int)

det_endyear = df_det['EYEAR'].tolist()
det_endmon = df_det['EMONTH'].tolist()
det_endday = df_det['EDAY'].tolist()

df_det['End_Time'] = df_det['End_Time'].astype(int)
det_endtime = df_det['End_Time'].tolist()

det_enddates = []

for y, m, d, t in zip(det_startyear, det_endmon, det_endday, det_endtime):
    if len(str(t)) <= 2:
        det_enddates.append(datetime(year=y, month=m, day=d, hour=0, minute=t))
    else:
        if len(str(t)) <= 3:
            det_enddates.append(datetime(year=y, month=m, day=d, hour=int(str(t)[0]), minute=int(str(t)[1:])))
        else:
            det_enddates.append(datetime(year=y, month=m, day=d, hour=int(str(t)[0:2]), minute=int(str(t)[2:])))

df_inc['DATETIME'] = inc_dates
df_det['START_DATETIME'] = det_startdates
df_det['END_DATETIME'] = det_enddates

det_lat = df_det['GOOD_LAT'].tolist()
det_lon = df_det['GOOD_LONG'].tolist()
inc_lat = df_inc['Lat'].tolist()
inc_lon = df_inc['Long'].tolist()

matches = []
counter = 1

for i, x, y in zip(inc_dates, inc_lon, inc_lat):
    print(counter)
    check = []
    matches.append(check)
    counter += 1
    for s, e, a, b in zip(det_startdates, det_enddates, det_lon, det_lat):
        if s <= i <= e and compare_distance(y, x, b, a, .1):
            check.append("TRUE")
            break
        else:
            check.append("FALSE")

match = []

for m in matches:
    if "TRUE" in m:
        match.append("TRUE")
    else:
        match.append("FALSE")

df_inc['MATCH_TENTH_KM'] = match

df_inc.to_csv('incidents-chunks/incidents_details_match5.csv', encoding='utf-8')