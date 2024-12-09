from flask import Flask
from dash import Dash, dcc, html, Input, Output

flask_app = Flask(__name__)

dash_app = Dash(
    __name__,
    server=flask_app,
    url_base_pathname="/"  # Serve Dash directly at root
)

dash_app.layout = html.Div(

    [
    html.H1("Dynamic Tableau Visualizations"),



    # Tabs for different Tableau visualizations
    dcc.Tabs(
        id="tabs",
        value="Tab 1",
        children=[
            dcc.Tab(label="Tab 1", value="Tab 1"),
            dcc.Tab(label="Tab 2", value="Tab 2"),
            dcc.Tab(label="Tab 3", value="Tab 3"),
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
    if selected_tab == "Tab 1": # GDP map
        with open("templates/vis.html", "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    if selected_tab == "Tab 2": # Volume by Infrastructure
        with open("templates/vis2.html", "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    if selected_tab == "Tab 3": # Optimal vs Actual Highway
        with open("templates/vis4.html", "r") as file:
            html_content = file.read()
        return html.Iframe(
            srcDoc=html_content,
            style={"width": "100%", "height": "800px", "border": "none"}
        )
    else:
        return html.Div(f"No visualization available for {selected_tab}.")


if __name__ == "__main__":
    flask_app.run(debug=True)
