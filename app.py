from dash import Dash
import dash_bootstrap_components as dbc

# Initialize app
app = Dash(
    __name__,
    use_pages=True,  # Enables multipage support
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server  # Needed for deployment (e.g. gunicorn/heroku)



# Run the server
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
