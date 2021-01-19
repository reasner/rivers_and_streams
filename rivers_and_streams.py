import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl

#Setup
cd = os.path.join(os.path.expanduser("~"),r'documents',r'projects',r'rivers_and_streams')
cd_dot_dot = os.path.join(os.path.expanduser("~"),r'documents',r'projects')

#Load boundary shapefiles
county_shapfile_path = os.path.join(cd_dot_dot,r'cfs_cz_shapefile_and_distances',r'fips','fips.shp')
county_map = gpd.read_file(county_shapfile_path)
county_map = county_map.to_crs("EPSG:5070")
cz_shapfile_path = os.path.join(cd_dot_dot,r'cfs_cz_shapefile_and_distances',r'cz00','cz00.shp')
cz_map = gpd.read_file(cz_shapfile_path)
cz_map = cz_map.to_crs("EPSG:5070")

#Load rivers and streams shapefile
rivers_and_streams_shapefile_path = os.path.join(cd,r'USA_Rivers_and_Streams-shp','9ae73184-d43c-4ab8-940a-c8687f61952f2020328-1-r9gw71.0odx9.shp')
rivers_and_streams = gpd.read_file(rivers_and_streams_shapefile_path)
rivers_and_streams = rivers_and_streams.to_crs("EPSG:5070")
rivers_and_streams = rivers_and_streams[~(rivers_and_streams['State'] == 'AK') & ~(rivers_and_streams['State'] == 'HI') & ~(rivers_and_streams['State'] == 'PR')]


#Collect river and stream data by county
rivers_and_streams = rivers_and_streams[rivers_and_streams['Name'].notna()]
fips = county_map['fips']
number_of_rivers_and_streams = []
length_of_rivers_and_streams = []
to_fips = []
for loc in fips:
    a = county_map[county_map['fips'] == str(loc)]
    keep = gpd.clip(rivers_and_streams,a)
    to_fips.append(str(loc))
    number_of_rivers_and_streams.append(len(keep['Name'].unique()))
    length_of_rivers_and_streams.append((keep.length.sum()/1000).round(2))

#Output by county data to .csv
river_data = pd.DataFrame(
    {'fips': to_fips,
     'number_rivers_and_streams': number_of_rivers_and_streams,
     'length_of_rivers_and_streams': length_of_rivers_and_streams
    })
river_data_path = os.path.join(cd,r'river_data.csv')
river_data.to_csv(river_data_path)

#Plot rivers
fig, ax = plt.subplots(1, figsize=(8.5,6.5))
ax.axis('off')
rivers_and_streams.plot(ax=ax,facecolor="none",linewidth=0.1,edgecolor='blue')
county_map.plot(ax=ax,facecolor="none",linewidth=0.1,edgecolor='gray')

rivers_and_streams_img_path = os.path.join(cd,r'rivers_and_streams.png')
plt.savefig(rivers_and_streams_img_path,bbox_inches='tight',pad_inches=0,dpi=300)





