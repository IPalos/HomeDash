from dash import html
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import datetime
from components.cardplot import CardPlot
from plotly.subplots import make_subplots


from theme import plot_colors

from pages.agua.agua_data import df

t1 = px.area(x=df['fecha'], y=df['gasto'])
t2 = px.area(x=df['fecha'], y=df['objetivo'])


fig = make_subplots().add_traces(t2.data )

layout = html.Div([
    CardPlot(fig)
    
])
