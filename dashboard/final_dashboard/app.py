from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = dbc.Container()

if __name__ == '__main__':
    app.run(debug=True)
