

from dash import html, dcc, page_container
import dash_bootstrap_components as dbc
from app import app
from components.sidebar import sidebar

# Custom CSS for enhanced design
custom_css = """

<style>
    :root {
        --bs-primary: #000000;
        --bs-link-color: #000000;
        --bs-link-hover-color: #333333;
        --bs-body-color: #000000;
        --bs-nav-link-color: #000000;
    }

    body {
        background: linear-gradient(135deg, #f8f8f8 0%, #d3d3d3 50%, #a8a8a8 100%),
                    repeating-linear-gradient(0deg, transparent, transparent 49px, rgba(0,0,0,0.05) 49px, rgba(0,0,0,0.05) 50px),
                    repeating-linear-gradient(90deg, transparent, transparent 49px, rgba(0,0,0,0.05) 49px, rgba(0,0,0,0.05) 50px);
        color: #000000;
    }

    .btn-primary {
        background-color: #000000 !important;
        border-color: #000000 !important;
        color: white !important;
    }
    .btn-primary:hover {
        background-color: #333333 !important;
        border-color: #333333 !important;
        color: white !important;
    }
    .text-primary {
        color: #000000 !important;
    }
    a {
        color: #000000 !important;
        text-decoration: none !important;
    }
    a:hover {
        color: #333333 !important;
    }

    .login-left { background: linear-gradient(45deg, #000000, #444444); color: #ffffff; padding: 50px; border-radius: 10px; }
    .login-card { background: #ffffff; color: #000000; border: 1px solid #cccccc; }
</style>

""" + """
<style>
    .nav-link-custom {
        text-decoration: none !important;
        color: #000000 !important;
        padding: 10px 15px !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        margin-bottom: 5px !important;
        display: block !important;
        border: none !important;
        background: transparent !important;
        width: 100% !important;
        text-align: left !important;
    }
    .nav-link-custom:hover {
        background-color: rgba(0,0,0,0.1) !important;
        color: #000000 !important;
        transform: translateX(3px) !important;
    }
    .nav-link-custom.active {
        color: #ffffff !important;
        font-weight: bold !important;
        background: #cccccc !important;
        box-shadow: none !important;
    }
    #sidebar-icon {
        color: white !important;
        transition: transform 0.3s ease !important;
    }
    #btn_sidebar {
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
        background: #000000 !important;
        border: none !important;
    }
    #btn_sidebar:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 3px 8px rgba(0,0,0,0.4) !important;
    }
</style>
"""

# Main layout: sidebar + content
app.layout = dbc.Container(
    fluid=True,
    className="px-0",
    children=[
        html.Div(custom_css, style={"display": "none"}),  # Inject custom CSS
        dcc.Location(id="url", refresh=False),
        dbc.Row(
            className="d-flex",
            children=[
                dbc.Col(
                    sidebar,
                    width=None,
                    className="col-md-2",
                    id="sidebar-col"
                ),
                dbc.Col(
                    html.Div(page_container, id="page-content", className="p-3"),
                    width=None,
                    className="col-md-10",
                    id="content-col"
                )
            ],
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
