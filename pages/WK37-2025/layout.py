# pages/home/layout.py
import dash
from dash import html


# Register the page
dash.register_page(
    __name__,
    path="/37",         # root path (default page)
    name="WK37-2025"       # name shown in sidebar
)

# Layout for the page
layout = html.Div(
    [
        html.H1("Welcome to WK37-2025"),
        html.P("Amazon Sales 2025")
    ]
)
