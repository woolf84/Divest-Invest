from mapbox import Geocoder
import pandas as pd

access_token = 'pk.eyJ1Ijoid29vbGY4NCIsImEiOiJja2dmdXN5cDAweHIzMnFsanl1c2czb3ljIn0.Ue5YNLPl14ybJnqV2BPjcw'
geocoder = Geocoder(access_token=access_token)
prox_lon = -71.093556
prox_lat = 42.315528
city = 'BOSTON'
geometries = []
lat = []
long = []
counter = 0
min_lon = -71.192279
min_lat = 42.227636
max_lon = -70.953671
max_lat = 42.399312

df = pd.read_csv('Second_Pass_Unique_Addresses.csv', encoding='utf-8')

addresses = df['address'].tolist()

for a in addresses:
    response = geocoder.forward(a + " " + city, lon=prox_lon, lat=prox_lat, limit=3)
    first = response.geojson()['features'][0]
    geo = [round(coord,6) for coord in first['geometry']['coordinates']]
    geometries.append(geo)
    print(counter)
    counter += 1

for g in geometries:
        long.append(g[0])
        long.append(g[1])

df['LAT'] = lat
df['LONG'] = long
df.to_csv('Second_Pass_Unique_Addresses_geo.csv', encoding='utf-8')


