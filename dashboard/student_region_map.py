from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json

app = Dash(__name__)

data_regions = {
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
studentdata_regions = pd.DataFrame(data_regions)

with open('./data/allregions.geojson', 'r') as file:
    geojson_regions = json.load(file)

data_regions_grouped = {
    "region": ['East Midlands',
               'North East',
               'Outline of Northern Ireland',
               'Scotland',
               'Eastern',
               'Wales',
               'West Midlands',
               'North Region',
               'South Region'
               ],
    "value": list(range(5,14)),
    }
studentdata_regions_grouped = pd.DataFrame(data_regions)

with open('./data/allregions_grouped.geojson', 'r') as file:
    geojson_regions_grouped = json.load(file)

# Layout
app.layout = html.Div([
    # Dropdown for selection
    html.Div([
        dcc.Dropdown(
            id='data-selector',
            options=[
                {'label': 'Regions', 'value': 'regions'},
                {'label': 'Groups', 'value': 'groups'}
            ],
            value='groups',
            style={'width': '200px', 'margin': '10px'}
        )
    ]),
    
    # Graph
    dcc.Graph(id='choropleth-map')
])

@callback(
    Output('choropleth-map', 'figure'),
    Input('data-selector', 'value')
)
def update_map(selected_data):
    # Select the appropriate dataset based on dropdown value
    if selected_data == 'regions':
        df = data_regions
        geojson = geojson_regions
    else:
        df = data_regions_grouped
        geojson = geojson_regions_grouped
    
    title = 'Regions Map'

    # Create the figure
    fig = px.choropleth_map(df, geojson=geojson, 
                            locations='region', 
                            color='value', 
                            featureidkey="properties.region",
                            color_continuous_scale="brwnyl",
                            range_color=(0, 12),
                            map_style="carto-positron",
                            zoom=4, center = {"lat": 55.6187, "lon": -1.3698},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    
    fig.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        title=title
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

