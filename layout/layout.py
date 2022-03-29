from dash import html, dcc

from layout.sidebar.sidebar import sidebar


# content = html.Div(id="page-content")
content = html.Div(
    id='page-content',
    className='main'
)

layout = html.Div([dcc.Location(id="url"), sidebar, content],className='layout')