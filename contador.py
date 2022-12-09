
import dash
from dash import html as dhtml
import dash_bootstrap_components as dbc

import datetime
import sys

app =  dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO], prevent_initial_callbacks= True, suppress_callback_exceptions=True)
data_inicial = "26-10-2022"
data_inicial_datetime = datetime.datetime.fromisoformat("2022-10-26")
today = datetime.datetime.today()
dif =(today - data_inicial_datetime)

app.layout =  dbc.Container([
                        dbc.Row([
                            dhtml.Div([
                                        dhtml.H1(children="DIA DA DESCOBERTA : {}".format(data_inicial), style={ 'color' : 'black', "margin": "10px", "padding": "10px"}),
                                    ], style={"background-color": "white", "margin": "5px", "padding": "0px"}),
                        ]),
                        dbc.Row([
                            dhtml.Div([
                                        dhtml.H1(children="DIAS SEM UMA CHANCE: {}".format(dif.days), style={ 'color' : 'black', "margin": "10px", "padding": "10px"}),
                                    ], style={"background-color": "white", "margin": "5px", "padding": "0px"}),
                        ]),
                        dbc.Row([
                            dhtml.Div([
                                        dhtml.Img(id="rosa", src=app.get_asset_url("rosa.png"), height=500),
                                    ], style={"background-color": "white", "margin": "5px", "padding": "0px"}),
                        ]),
                ])


server = app.server
if __name__ == "__main__":
    if len(sys.argv) > 1:
        app.run_server(debug=True)
    else:
        app.run_server(debug=True)
