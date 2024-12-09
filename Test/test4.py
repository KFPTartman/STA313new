from dash import Dash, dcc, html, Input, Output

# Initialize Dash app
app = Dash(__name__)

# HTML templates for Tableau visualizations
tableau_html = {
    "Tab 1": """
<html>
    <head>
        <title> Tableau Dashboard Demo </title>
    </head>
    <body>
        <h5> This is for testing purposes</h5>
        <div class='tableauPlaceholder' id='viz1733353414953' style='position: relative'>
            <noscript>
                <a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Infrastructure-Highway&#47;Dashboard1&#47;1_rss.png' style='border: none' />
                </a>
            </noscript>
            <object class='tableauViz'  style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='embed_code_version' value='3' />
                <param name='site_root' value='' />
                <param name='name' value='Infrastructure-Highway&#47;Dashboard1' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
                <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;In&#47;Infrastructure-Highway&#47;Dashboard1&#47;1.png' />
                <param name='animate_transition' value='yes' />
                <param name='display_static_image' value='yes' />
                <param name='display_spinner' value='yes' />
                <param name='display_overlay' value='yes' />
                <param name='display_count' value='yes' />
                <param name='language' value='en-US' />
            </object>
        </div>
</html>
    """,
    "Tab 2": """
        <div class='tableauPlaceholder' id='viz2' style='position: relative'>
            <noscript>
                <a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;SomeOtherViz&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a>
            </noscript>
            <object class='tableauViz' style='display:none;'>
                <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                <param name='name' value='SomeOtherViz&#47;Dashboard2' />
                <param name='tabs' value='no' />
                <param name='toolbar' value='yes' />
            </object>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz2');
            var vizElement = divElement.getElementsByTagName('object')[0];
            vizElement.style.width = '1000px';
            vizElement.style.height = '827px';
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
    """,
}

# App layout
app.layout = html.Div([
    html.H1("Dynamic Tableau Visualizations", style={"textAlign": "center"}),

    # Tabs for different Tableau visualizations
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

    # Container for Tableau visualization
    html.Div(id="tabContent", style={"marginTop": "20px"})
])

# Callback to dynamically update Tableau visualization
@app.callback(
    Output("tabContent", "children"),
    [Input("tabs", "value")]
)
def update_visualization(selected_tab):
    return dcc.Markdown(
        tableau_html[selected_tab],
        dangerously_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

