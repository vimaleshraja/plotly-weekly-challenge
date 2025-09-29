from dash import html, dcc, Input, Output, State
import dash
import dash_bootstrap_components as dbc
from app import app  # import app instance

# --- Sidebar styles ---
EXPANDED_STYLE = {
    "height": "100vh",
    "background-color": "#f8f9fa",
    "padding": "10px",
    "width": "220px",
    "transition": "width 0.3s",
    "overflow": "hidden"
}

COLLAPSED_STYLE = {
    "height": "100vh",
    "background-color": "#f8f9fa",
    "padding": "10px 5px",
    "width": "60px",
    "transition": "width 0.3s",
    "overflow": "hidden"
}

# --- Sidebar Layout ---
sidebar = html.Div(
    id="sidebar",
    children=[
        dbc.Button("☰", id="btn_sidebar", outline=True, color="secondary", className="mb-2"),
        html.Div(id="sidebar-content")  # content populated by callback
    ],
    style=EXPANDED_STYLE,
)

# --- Callbacks ---

# 1. Toggle collapse/expand
@app.callback(
    Output("sidebar", "style"),
    Output("sidebar-content", "children"),
    Input("btn_sidebar", "n_clicks"),
    prevent_initial_call=True
)
def toggle_sidebar(n_clicks):
    # Odd clicks → collapsed
    if n_clicks and n_clicks % 2 == 1:
        return COLLAPSED_STYLE, None

    # Expanded state
    content = [
        html.H2("Navigation", className="display-6"),
        dcc.Input(
            id="search-bar", type="text", placeholder="Search pages...",
            className="mb-2", style={"width": "100%"}
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(page["name"], href=page["path"], active="exact")
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            id="sidebar-links"
        )
    ]
    return EXPANDED_STYLE, content


# 2. Filter pages dynamically
@app.callback(
    Output("sidebar-links", "children"),
    Input("search-bar", "value"),
    prevent_initial_call=True
)
def filter_pages(search_value):
    if not search_value:
        pages = dash.page_registry.values()
    else:
        search_value = search_value.lower()
        pages = [p for p in dash.page_registry.values() if search_value in p["name"].lower()]

    return [
        dbc.NavLink(page["name"], href=page["path"], active="exact")
        for page in pages
    ]
