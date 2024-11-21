from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json

app = Dash(__name__)

data = {
    "region": ['North East',
    'North West',
    'Yorkshire and The Humber',
    'East Midlands',
    'West Midlands',
    'Eastern',
    'London',
    'South East',
    'South West',
    'Scotland',
    'Wales',
    'Outline of Northern Ireland'],
    "value": list(range(1,13)),
    }
studentdata = pd.DataFrame(data)

with open('./data/combined_geojson.geojson', 'r') as file:
    geojson = json.load(file)


fig = px.choropleth_map(studentdata, geojson=geojson, locations='region', color='value', featureidkey="properties.NAME",
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           map_style="carto-positron",
                           zoom=4, center = {"lat": 55.6187, "lon": -1.3698},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


