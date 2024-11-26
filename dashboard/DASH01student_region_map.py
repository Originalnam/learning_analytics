import json
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
from dashboard_functions import get_map_data

app = Dash(__name__)

with open('./data/dashboard/allregions_grouped.geojson', 'r') as file:
    geojson_regions_grouped = json.load(file)

student_data = get_map_data()    
print(student_data)

# Layout
app.layout = html.Div([
    # Dropdown for selection
    html.Div([
        dcc.RadioItems(
            id='map-selector', 
            options=[
                {'label': 'Regions', 'value': 'regions'},
                {'label': 'Grouped regions', 'value': 'groups'}
            ],
            value="groups",
            inline=True
            )
        ]),
    
    # Graph
    dcc.Graph(id='choropleth-map')
])

@callback(
    Output('choropleth-map', 'figure'),
    Input('map-selector', 'value')
)
def update_map(selected_data):
    title = 'Regions Map'

    # Create the figure
    fig = px.choropleth_map(student_data, geojson=geojson_regions_grouped, 
                            locations='region', 
                            color='value', 
                            featureidkey="properties.region",
                            color_continuous_scale="brwnyl",
                            range_color=(min(student_data['value']), max(student_data['value'])),
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

