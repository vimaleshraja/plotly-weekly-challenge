# pages/home/layout.py
import dash
from dash import html

# Register the page
dash.register_page(
    __name__,
    path="/36",         # root path (default page)
    name="WK36-2025"       # name shown in sidebar
)

# Layout for the page
layout = html.Div(
    [
        html.H1("Welcome to WK36-2025"),
        html.P("Week 36")
        
    ]
)
