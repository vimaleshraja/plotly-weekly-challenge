from dash import Dash
import dash_bootstrap_components as dbc

# Initialize app
app = Dash(
    __name__,
    use_pages=True,  # Enables multipage support
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ]
)

server = app.server  # Needed for deployment (e.g. gunicorn/heroku)
