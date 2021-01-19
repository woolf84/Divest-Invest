import pandas as pd
import geopandas

df = pd.read_csv('test_output.csv',encoding='utf-8-sig')
gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['LONG'], df['LAT']))
gdf.to_file("test.geojson", driver='GeoJSON')
