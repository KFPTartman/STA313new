from dash import Dash, dcc, html
from dash.dependencies import Output, Input

# Initialize the Dash app
app = Dash(__name__)

# Tableau embed URLs
tableau_urls = {
    "Tab 1": "https://public.tableau.com/views/Infrastructure-Highway/Dashboard1?:embed=y&:language=en-US&:display_count=n&:origin=viz_share_link",
    "Tab 2": "https://public.tableau.com/views/YourViz2URL",
    "Tab 3": "https://public.tableau.com/views/YourViz3URL",
    "Tab 4": "https://ublic.tableau.com/views/Infrastructure-Highway/Dashboard1?:embed=y&:language=en-US&:display_count=n&:origin=viz_share_link",
}

# Define the app layout
app.layout = html.Div([
    dcc.Tabs(
        id="tabs",
        value="Tab 1",
        children=[
            dcc.Tab(label="Tab 1", value="Tab 1"),
            dcc.Tab(label="Tab 2", value="Tab 2"),
            dcc.Tab(label="Tab 3", value="Tab 3"),
            dcc.Tab(label="Tab 4", value="Tab 4"),
        ]
    ),
    html.Div(id="content"),
])

# Define callback to update content based on selected tab
@app.callback(
    Output("content", "children"),
    [Input("tabs", "value")]
)
def update_content(tab_name):
    return html.Iframe(
        src="https://public.tableau.com/views/Infrastructure-Highway/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
        style={"width": "100%", "height": "600px", "border": "none"}
    )

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
