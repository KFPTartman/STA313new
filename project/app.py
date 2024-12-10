from flask import Flask
from dash import Dash, dcc, html, Input, Output

from flask import Flask
import os

flask_app = Flask(__name__)

dash_app = Dash(
    __name__,
    server=flask_app,
    url_base_pathname="/"  # Serve Dash directly at root
)

dash_app.layout = html.Div(

    [
    html.H1("Development of Transportation in China"),

    # Tabs for different Tableau visualizations
    dcc.Tabs(
        id="tabs",
        value="Tab 1",
        children=[
            dcc.Tab(label="1. Overview of Passenger Volume", value="Tab 1"),
            dcc.Tab(label="2. Highway Infrastructure", value="Tab 2"),
            dcc.Tab(label="3. Permanent", value="Tab 3"),
            dcc.Tab(label="4. Highway Development Envision", value="Tab 4"),
        ]
    ),

    # Container for Tableau visualization
    html.Div(id="tabContent")
])

# Callback to dynamically load Tableau visualization
@dash_app.callback(
    Output("tabContent", "children"),
    [Input("tabs", "value")]
)

def update_visualization(selected_tab):
    # Get the base directory dynamically
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if selected_tab == "Tab 1":  # GDP map
        file_path = os.path.join(base_dir, "templates", "vis2.html")
        with open(file_path, "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    if selected_tab == "Tab 2":  # Volume by Infrastructure
        file_path = os.path.join(base_dir, "templates", "vis.html")
        with open(file_path, "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    if selected_tab == "Tab 3":  # Some vis that I don't know yet
        file_path = os.path.join(base_dir, "templates", "vis4.html")
        with open(file_path, "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    if selected_tab == "Tab 4":  # Optimal vs Actual Highway
        file_path = os.path.join(base_dir, "templates", "vis4.html")
        with open(file_path, "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    else:
        return html.Div(f"No visualization available for {selected_tab}.")


if __name__ == "__main__":
    flask_app.run(debug=True)
