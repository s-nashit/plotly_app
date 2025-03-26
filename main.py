import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

data = {
    'area' : [100,200,300,400,500,600,700,750,800,900,1000],
    'cost' : [98, 150, 200, 250, 300, 350, 412, 459, 507, 567, 600]
}

df = pd.DataFrame(data)

app.layout = html.Div([html.H1('My Application'),
html.H2('Area vs Cost Graph'),
dcc.Dropdown(
    id = 'graph_type',
    options = [
        {'label': 'Line Plot', 'value' : 'line'},
        {'label': 'Bar Plot', 'value' : 'bar'},
        {'label': 'Scatter Plot', 'value' : 'scatter'}
    ]
),
dcc.Graph(id = 'graph')],
                      style={'textAlign': 'center',
                             'color': 'red',
                             'backgroundColor': 'lightblue'})


@app.callback(
    Output('graph', 'figure'),
    [Input('graph_type', 'value')]
)

def update_graph(graph_type):
    if graph_type == 'line':
        fig = px.line(df, x = 'area', y='cost')
    elif graph_type == 'bar':
        fig = px.bar(df, x = 'area', y='cost')
    else:
        fig = px.scatter(df, x = 'area', y='cost')
    
    return fig


app.run(debug=True, port:5050)
