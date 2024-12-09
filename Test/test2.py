from dash import Dash, dcc, html
from dash.dependencies import Output, Input

# Initialize the Dash app
app = Dash(__name__)

# HTML Embed Code for Tableau Visualizations
tableau_embeds = {
    "Tab 1": """
        <iframe src="https://public.tableau.com/views/Infrastructure-Highway/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
                width="100%" height="600" frameborder="0"></iframe>
    """,
    "Tab 2": """
        <iframe src="https://public.tableau.com/views/Salesforce20Sales20Cloud20-20Weighted20Sales20Pipeline_17333508028400/Home?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
                width="100%" height="600" frameborder="0"></iframe>
    """,
    "Tab 3": """
        <iframe src="https://www.youtube.com/watch?v=wJ2CHIJalNU"
                width="100%" height="600" frameborder="0"></iframe>
    """,
    "Tab 4": """
        <iframe src="https://onlinesequencer.net/4178603"
                width="100%" height="600" frameborder="0"></iframe>
    """,
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

# Callback to render Tableau visualization based on selected tab
@app.callback(
    Output("content", "children"),
    [Input("tabs", "value")]
)
def update_content(tab_name):
    return dcc.Markdown(
        tableau_embeds[tab_name],
        dangerously_allow_html=True
    )

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)

