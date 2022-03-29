import dash_bootstrap_components as dbc
from dash import html

from utils.constants import *


# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Dashboard Santander", className="display-4"),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ],

)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Nav(
            [
                dbc.NavLink("Agua", href=agua_page, active="exact"),
            ],
            vertical=True,
        ),
    ],
    id="sidebar",
    className='sidenav'
)