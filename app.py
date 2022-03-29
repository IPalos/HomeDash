from dash import Dash, html, dcc , callback, Input, Output
import dash_bootstrap_components as dbc

from layout.layout import layout

from utils.constants import *

from pages.agua import agua

import flask


server = flask.Flask(__name__) # define flask app.server

app = Dash(
    __name__,
    suppress_callback_exceptions=True, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)


app.layout = layout


@callback(
  Output("page-content", "children"), 
  Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == agua_page:
        return agua.layout
    # No hay pagina
    return html.P('ERROR 404')

if __name__ == '__main__':
    app.run_server(debug=True)