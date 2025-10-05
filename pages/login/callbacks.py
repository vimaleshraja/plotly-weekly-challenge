from dash import Input, Output, State, html
import dash

# Import the app instance
from app import app

@app.callback(
    [
        Output("login-output", "children"),
        Output("login-redirect", "href")
    ],
    Input("btn-login", "n_clicks"),
    State("login-email", "value"),
    State("login-password", "value"),
    prevent_initial_call=True
)
def handle_login(n_clicks, email, password):
    if email and password:
        # Simple mock authentication: accept if email contains "@"
        if "@" in email:
            return html.Div("Login successful! Redirecting...", className="text-success"), "/"
        else:
            return html.Div("Invalid email.", className="text-danger"), dash.no_update
    return html.Div("Please enter both email and password.", className="text-warning"), dash.no_update
