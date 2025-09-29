import dash
from dash import html

# Register page at root URL
dash.register_page(__name__, path="/", name="Home")

layout = html.Div(
    [
        html.H1("Welcome to Plotly Weekly Tasks", className="display-4"),
        html.P("This is your dashboard home page.", className="lead"),
    ],
    style={"padding": "20px"}
)
