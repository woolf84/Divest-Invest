import json
import geopandas as gpd
import shapely
from shapely.geometry import shape, Point
# depending on your version, use: from shapely.geometry import shape, Point

# load GeoJSON file containing sectors
census = gpd.read_file('Census_2010_Tracts.geojson')
details = gpd.read_file('Details_2019_C_Latlng_Chunks/Details_2019_C_latlng_chunk5.csv')

#details['Pay_Amount'] = details['Pay_Amount'].astype(int)
#details_pay = details['Pay_Amount'].tolist()
details['GOOD_LONG'] = details['GOOD_LONG'].astype(float)
details_long = details['GOOD_LONG'].tolist()
details['GOOD_LAT'] = details['GOOD_LAT'].astype(float)
details_lat = details['GOOD_LAT'].tolist()
details_points = []

census_geo = census['geometry'].tolist()
census_geoid = census['GEOID10'].tolist()
details_geoid = []

for x, y in zip(details_long, details_lat):
    details_points.append(Point(x, y))

c = 0

for p in details_points:
    counter = 0
    print(c)
    c += 1
    for g, i in zip(census_geo, census_geoid):
        g = shape(g)
        if counter == len(census_geo) - 1:
            if g.contains(p):
                details_geoid.append(i)
            else:
                details_geoid.append('NA')
        else:
            if g.contains(p):
                details_geoid.append(i)
                break
            else:
                counter += 1

details['GEOID10'] = details_geoid

details.to_csv('Details_2019_C_Latlng_Chunks/Chunk5-output.csv', encoding='utf-8')

# construct point based on lon/lat returned by geocoder
#point = Point(-122.7924463, 45.4519896)

# check each polygon to see if it contains the point
#for feature in js['features']:
#    polygon = shape(feature['geometry'])
#    if polygon.contains(point):
#        print('Found containing polygon:', feature)

