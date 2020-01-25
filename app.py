#!/usr/bin/python3
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from qhue_manager import HueController

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Textarea(
        id='color-log'
    ),
    dcc.Slider(
        id='color-temp-slider',
        min=100,
        max=4000,
        value=300,
        step=10
    )
])

@app.callback(
    Output('color-log', "value"),
    [Input('color-temp-slider', 'value')])
def update_figure(temperature_value):
    hc.setLightTemp(6, ct=temperature_value)
    return "Color temp is now {}".format(temperature_value)

if __name__ == '__main__':
    hc = HueController()
    hc.listLights()
    app.run_server(debug=True, port =8080, host='0.0.0.0')