import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/login", name="Login")

layout = dbc.Container(
    fluid=True,
    className="vh-100",
    children=[
        dcc.Location(id="login-redirect", refresh=True),
        dbc.Row(
            className="h-100",
            children=[
                dbc.Col(
                    html.Div(
                        [
                            html.H1("About This App", className="display-4 mb-4"),
                            html.P("This is a Plotly Weekly Challenges Dashboard for creating and managing interactive data visualizations.", className="lead mb-3"),
                            html.P("Track your weekly progress on tasks and build stunning plots with ease.", className="lead")
                        ],
                        className="login-left d-flex flex-column justify-content-center h-100"
                    ),
                    width=6
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H2("Login", className="card-title text-center mb-4"),
                                    dbc.Form(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Label("Email", html_for="login-email", width=12),
                                                    dbc.Col(
                                                        dbc.Input(
                                                            type="email",
                                                            id="login-email",
                                                            placeholder="Enter email address",
                                                            required=True,
                                                        ),
                                                        width=12,
                                                        className="mb-3"
                                                    ),
                                                ]
                                            ),
                                            dbc.Row(
                                                [
                                                    dbc.Label("Password", html_for="login-password", width=12),
                                                    dbc.Col(
                                                        dbc.Input(
                                                            type="password",
                                                            id="login-password",
                                                            placeholder="Enter password",
                                                            required=True,
                                                        ),
                                                        width=12,
                                                        className="mb-3"
                                                    ),
                                                ]
                                            ),
                                            dbc.Button("Login", id="btn-login", color="primary", className="w-100"),
                                            html.Div(id="login-output", className="mt-3 text-center")
                                        ]
                                    ),
                                ]
                            ),
                        ],
                        className="login-card w-75 mx-auto"
                    ),
                    width=6,
                    className="d-flex align-items-center justify-content-center"
                )
            ]
        ),
    ],
)
