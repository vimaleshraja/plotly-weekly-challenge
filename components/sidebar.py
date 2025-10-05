from dash import html, dcc, Input, Output
import dash
import dash_bootstrap_components as dbc
from app import app  # import app instance

# --- Sidebar styles ---
EXPANDED_STYLE = {
    "height": "100vh",
    "background": "radial-gradient(circle, #f0f0f0, #d0d0d0)",
    "padding": "10px",
    "width": "220px",
    "overflow": "hidden"
}

COLLAPSED_STYLE = {
    "height": "100vh",
    "background": "radial-gradient(circle, #f0f0f0, #d0d0d0)",
    "padding": "8px 3px",
    "width": "45px",
    "overflow": "hidden",
    "text-align": "center",
    "display": "flex",
    "align-items": "center",
    "flex-direction": "column"
}

# --- Sidebar Layout ---
sidebar = html.Div(
    id="sidebar",
    children=[
        dbc.Button([
            html.I(className="fas fa-chevron-right", id="sidebar-icon", style={"color": "white", "font-size": "12px"})
        ], id="btn_sidebar", outline=True, color="secondary", className="mb-2", style={"width": "32px", "height": "32px", "border": "none", "background": "#000000", "display": "flex", "align-items": "center", "justify-content": "center"}),
        html.Div(id="sidebar-content")  # content populated by callback
    ],
    style=COLLAPSED_STYLE,
)

# Helper function for sidebar content
def get_navigation_content():
    pages = [p for p in dash.page_registry.values() if p["path"] != "/login"]  # Exclude login page
    return [
        html.H2("Navigation", className="display-6", style={"font-size": "1.2rem", "color": "#000000"}),
        dcc.Input(
            id="search-bar",
            type="text",
            placeholder="Search pages...",
            className="mb-3",
            style={"width": "100%", "border-radius": "5px", "border": "1px solid #ced4da"}
        ),
        html.Hr(style={"margin": "15px 0"}),
        dbc.Nav(
            [
                dbc.NavLink(
                    html.Span([
                        html.I(className="fas fa-file-alt me-2"),
                        page["name"]
                    ]),
                    href=page["path"],
                    active="exact",
                    className="nav-link-custom",
                    style={"color": "black", "text-decoration": "none"}
                )
                for page in pages
            ],
            vertical=True,
            pills=True,
            id="sidebar-links"
        )
    ]

@app.callback(
    Output("sidebar", "style"),
    Output("sidebar-col", "style"),
    Output("content-col", "style"),
    Output("sidebar-content", "children"),
    Output("sidebar-icon", "className"),
    Input("btn_sidebar", "n_clicks"),
    Input("url", "pathname")
)
def toggle_sidebar(n_clicks, pathname):
    if pathname == "/login":
        content = None
        sidebar_col_style = {"display": "none"}
        content_col_style = {"flex": "1"}
        icon = "fas fa-chevron-right"
        sidebar_style = COLLAPSED_STYLE
    elif n_clicks is None or n_clicks % 2 == 0:
        # Closed: narrow sidebar
        content = None
        sidebar_col_style = {"flex": "0", "width": "45px"}
        content_col_style = {"flex": "1"}
        icon = "fas fa-chevron-right"
        sidebar_style = COLLAPSED_STYLE
    else:
        # Open: show sidebar content
        content = get_navigation_content()
        sidebar_col_style = {"flex": "0", "width": "220px"}
        content_col_style = {"flex": "1"}
        icon = "fas fa-chevron-left"
        sidebar_style = EXPANDED_STYLE
    return sidebar_style, sidebar_col_style, content_col_style, content, icon

# Filter menu dynamically
@app.callback(
    Output("sidebar-links", "children"),
    Input("search-bar", "value"),
    prevent_initial_call=True
)
def filter_menu(search_value):
    pages = [p for p in dash.page_registry.values() if p["path"] != "/login"]
    if not search_value:
        items = [(p["name"], p["path"]) for p in pages]
    else:
        search_value = search_value.lower()
        items = [(p["name"], p["path"]) for p in pages if search_value in p["name"].lower()]
    
    return [
        dbc.NavLink(
            html.Span([
                html.I(className="fas fa-file-alt me-2"),
                name
            ]),
            href=href,
            active="exact",
            className="nav-link-custom",
            style={"color": "black", "text-decoration": "none"}
        )
        for name, href in items
    ]
