# add project root to Python pathimport sys
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import os
import pandas as pd
import geopandas as gpd
from urllib.request import urlopen
from general_functions import load_data

script_dir = os.path.dirname(os.path.abspath(__file__))

# load data
load_path = os.path.join(script_dir, '../data/', 'EDA/')
dfs = load_data(load_path)

# load geoJSON files
gdfGB = gpd.GeoDataFrame.from_file('https://raw.githubusercontent.com/martinjc/UK-GeoJSON/refs/heads/master/json/electoral/gb/eer.json')
gdfGB.rename(columns={"EER13NM": "region"}, inplace=True)
gdfNI = gpd.GeoDataFrame.from_file('https://raw.githubusercontent.com/martinjc/UK-GeoJSON/refs/heads/master/json/electoral/ni/eer.json')
gdfNI.rename(columns={"NAME": "region"}, inplace=True)

# combine geoJSON and group regions
regions_mapping_combined = {'North East': 'North Region',
                            'Eastern': 'South Region',
                            'Scotland': 'Scotland',
                            'North West': 'North Region',
                            'South East': 'South Region',
                            'West Midlands': 'West Midlands',
                            'Wales': 'Wales',
                            'Outline of Northern Ireland': 'Outline of Northern Ireland',
                            'South West': 'South Region',
                            'East Midlands': 'East Midlands',
                            'Yorkshire and The Humber': 'North Region',
                            'London': 'South Region'
                            }
combined_gdf = gpd.GeoDataFrame(pd.concat([gdfGB, gdfNI], ignore_index=True))
combined_gdf.loc[:,'group'] = combined_gdf['region'].map(regions_mapping_combined)
combined_gdf.drop(['EER13CD', 'EER13CDO', 'ID', 'Area_SqKM','OBJECTID'], axis=1, inplace=True)

grouped_gdf = combined_gdf.dissolve(by='group').reset_index()
grouped_gdf['region'] = grouped_gdf['group']
grouped_gdf.drop('group', axis=1, inplace=True)

# save geoJSON
write_path = os.path.join(script_dir, '../data/', 'dashboard/', 'allregions_grouped.geojson')
grouped_gdf.to_file(write_path, 
                    driver='GeoJSON')
