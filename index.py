from dash import html, dcc, page_container
import dash_bootstrap_components as dbc
from app import app
from components.sidebar import sidebar

# Main layout: sidebar + content
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row([
            dbc.Col(
                sidebar,
                width=2,
                id="sidebar-col"
            ),
            dbc.Col(
                html.Div(page_container, id="page-content", className="p-4"),
                width=10
            )
        ])
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
