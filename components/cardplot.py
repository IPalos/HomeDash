from dash import html, dcc
import dash_bootstrap_components as dbc

def CardPlot(fig):
	return html.Div([
            dbc.Card(
                dbc.CardBody([
                    dcc.Graph(
                        figure=fig
                    ),
                ]),
                className='card-plot'
            ),
        ])
