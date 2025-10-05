import dash
from dash import html

# Register page at root URL
dash.register_page(__name__, path="/", name="Home")

layout = html.Div(
    [
        html.H1("Welcome to Home"),
        html.P("Dashboard Overview")
    ]
)
