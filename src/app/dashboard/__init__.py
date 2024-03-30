from dash import Dash, html, dcc
from pandas import DataFrame
from plotly import express
from flask import Flask


df = DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)

fig = express.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


def init_dashboard(app: Flask):
    dashboard = Dash(
        server=app,
        routes_pathname_prefix="/dashboard/",
    )

    dashboard.layout = html.Div(
        children=[
            html.H1(children="Hello Dash"),
            html.Div(
                children="""
            Dash: A web application framework for your data.
        """
            ),
            dcc.Graph(id="example-graph", figure=fig),
        ]
    )

    return dashboard.server
