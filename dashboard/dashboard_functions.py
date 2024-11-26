import os
import pandas as pd

def get_path_dashboard_data():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_dashboard_data = os.path.join(project_root, 'data', 'dashboard')
    return path_dashboard_data

def get_map_data(df=None):
    regions_name_mapping = {
        'East Anglian Region': 'South Region',
        'Scotland': 'Scotland',
        'North Western Region': 'North Region',
        'South East Region': 'South Region',
        'West Midlands Region': 'West Midlands',
        'Wales': 'Wales',
        'Ireland': 'Outline of Northern Ireland',
        'South West Region': 'South Region',
        'East Midlands Region': 'East Midlands',
        'Yorkshire Region': 'North Region',
        'London Region': 'South Region'
        }
    
    if not df:
        df = pd.read_csv(os.path.join(get_path_dashboard_data(), 'studentinfo.csv'))
    else:
        df = df.copy()

    df['region'] = df['region'].map(lambda x: regions_name_mapping.get(x, x))
    region_counts = df['region'].value_counts().reset_index()

    data_grouped_region = {
    'region': region_counts['region'].tolist(),
    'value': region_counts['count'].tolist()
    }
    
    return data_grouped_region
