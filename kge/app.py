# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html as inner_html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go

import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
from kge import providers
from kge import handlers
from kge import interfacers

converter = handlers.TempConverter()
provider = providers.NeoProvider()
interfacer = interfacers.PythonInterfacer()

def get_field(data):
    for record in data:
        for key in record.keys():
            return record[key]

def get_df_from_text(text):
    cypher_query = converter.convert(text)
    data = provider.execute(cypher_query)
    command = get_field(data)
    return {
        'command' : command,
        'df': interfacer.execute(command)
    }

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Perception'
df = None

app.layout = html.Div([
    html.H2(children=app.title, style={
        'textAlign': 'center',
        'color': '#32B232'
    }),
    dcc.Input(id='input-1-submit', type='text', placeholder='What would you like to visualize today?', style={
        'width': '100%'
    }),
    html.Div(id='output-submit')
])

@app.callback(
    Output('output-submit', 'children'),
    [Input('input-1-submit', 'n_submit'), Input('input-1-submit', 'n_blur')],
    [State('input-1-submit', 'value')])
def update_output(ns1, nb1, input1):
    if input1 is None:
        return ''

    data = get_df_from_text(input1)
    df = data['df']
    return [inner_html.DangerouslySetInnerHTML(data['command']),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )]


if __name__ == '__main__':
    app.run_server(debug=True)