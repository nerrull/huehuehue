import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html

import itertools
import datetime


from dummy_db import DummyDB
 
def generate_output_callback(room):
    def output_callback(light_value):
        # This function can display different outputs depending on
        # the values of the dynamic controls
        return '''
            Light {}, room {} 
            '''.format(
                light_value,
                room,
                )
    return output_callback


def create_light_controls(db):
    light_controls = {}
    for room in db.get_rooms():
        lights=  db.get_lights(room)
        light_controls[room] ={}

        for light in lights:
            light_component_id = "{}_{}_on".format(room, light)
            light_output_id = light_component_id +"_output"
            light_controls[room][light]   = html.Div([
                html.Span('Light {} '.format(light)),

                daq.BooleanSwitch(
                id=light_component_id,
                on=True),
                html.Div('Light output', id =light_output_id) ])
            # create a callback for each lightswitch
            app.callback(
                Output(light_output_id, 'children'),
                [Input(light_component_id, 'on')])(
                generate_output_callback(room)
            )
    return light_controls

def create_app(app, db):
    app.layout = html.Div([
        html.Hr(),
        html.Div(id='live-update-text',
             style={'font-size': '10px'}),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        ),
        dcc.Dropdown(
            id='Room',
            options=[
                {'label': i, 'value': i} for i in db.get_rooms()
            ],
            value="Salon"
        ),
        html.Hr(),
        html.Div('Dynamic Controls'),
        html.Div(
            id='controls-container'
        ),
        html.Hr(),
        html.Div('Output'),
        html.Div(
            id='output-container'
        )
    ])

    db.set_elements_dict(create_light_controls(db))


    def generate_control_id(value):
        return 'Control {}'.format(value)

    @app.callback(
        Output('controls-container', 'children'),
        [Input('Room', 'value')])
    def display_light_controls(value):
        # generate 2 dynamic controls based off of the datasource selections
        print ("getting elements for {}".format(value))

        return html.Div(list(db.get_room_elements(value).values()) )

    def generate_output_id(value1):
        return '{} container'.format(value1)

    @app.callback(
        Output('output-container', 'children'),
        [Input('Room', 'value')])
    def display_controls2(datasource_1_value):
        # create a unique output container for each pair of dyanmic controls
        return html.Div(id=generate_output_id(
            datasource_1_value
        ))

   
        
    # each unique dynamic control pairing is linked to a dynamic output component



    @app.callback(Output('live-update-text', 'children'),
                [Input('interval-component', 'n_intervals')])
    def update_date(n):
        return [html.P('Last updated ' +str(datetime.datetime.now()))]

if __name__ == '__main__':
    db = DummyDB()
    app = dash.Dash(suppress_callback_exceptions = True)
    create_app(app, db)
    app.run_server(debug=True)