import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
import altair as alt
import vega_datasets
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, assets_folder='assets', external_stylesheets=[dbc.themes.CERULEAN])
app.config['suppress_callback_exceptions'] = True

server = app.server
app.title = 'Group112 Dash app: Unemployment'

def make_plot(start_year = 2000, end_year = 2001, stat = 'rate'): #Add in a default value to start with


    #THEME
    def mds_special():
        font = "Arial"
        axisColor = "#000000"
        gridColor = "#DEDDDD"
        return {
            "config": {
                "title": {
                    "fontSize": 24,
                    "font": font,
                    "anchor": "start", # equivalent of left-aligned.
                    "fontColor": "#000000"
                },
                'view': {
                    "height": 300, 
                    "width": 400
                },
                "axisX": {
                    "domain": True,
                    #"domainColor": axisColor,
                    "gridColor": gridColor,
                    "domainWidth": 1,
                    "grid": False,
                    "labelFont": font,
                    "labelFontSize": 12,
                    "labelAngle": 0, 
                    "tickColor": axisColor,
                    "tickSize": 5, # default, including it just to show you can change it
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "X Axis Title (units)", 
                },
                "axisY": {
                    "domain": False,
                    "grid": True,
                    "gridColor": gridColor,
                    "gridWidth": 1,
                    "labelFont": font,
                    "labelFontSize": 14,
                    "labelAngle": 0, 
                    #"ticks": False, # even if you don't have a "domain" you need to turn these off.
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "Y Axis Title (units)", 
                    # titles are by default vertical left of axis so we need to hack this 
                    #"titleAngle": 0, # horizontal
                    #"titleY": -10, # move it up
                    #"titleX": 18, # move it to the right so it aligns with the labels 
                },
            }
                }

    # register the custom theme under a chosen name
    alt.themes.register('mds_special', mds_special)

    # enable the newly registered theme
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default

    #READ IN DATA
    df_raw = pd.read_csv('../data/unemply_df_year.csv', index_col=0)
    df = df_raw.drop(columns = ['count', 'rate'])
    df = df_raw.pivot(index = 'series', columns = 'year', values = 'total').reset_index()

    new_df = pd.DataFrame(df["series"])
    if stat == "rate":
        new_df["growth_{0}_{1}".format(start_year, end_year)] = (df[end_year] - df[start_year]) / df[start_year]
    if stat == "count":
        new_df["difference_{0}_{1}".format(start_year, end_year)] = df[end_year] - df[start_year]
        
    #PLOT 1 JOB GROWTH ACROSS INDUSTRIES
    chart = alt.Chart(new_df).mark_bar(size=4).encode(
                alt.X(new_df.columns[1], type = 'quantitative', title = stat),
                alt.Y("series:O", title=""),
                tooltip = [new_df.columns[1]]
            ).properties(title='Job Growth Across Industries',
                        width=600, height=400).interactive()

    return chart

header = dbc.Jumbotron(
    [
        dbc.Container(
            [html.H1("Unemployment Rates in Industries", className="display-3"),
                html.P("These graphs display a framework for countries to examine their unemployment rates across industries",
                    className="lead",
                ),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

content = dbc.Container([
    dbc.Row(
                [dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot',
                        height='500',
                        width='1000',
                        style={'border-width': '0'},
                        ################ The magic happens here
                        srcDoc=make_plot().to_html()
                        ################ The magic happens here
                        )),

                             # Just to add some space
                    html.Iframe(height='100', width='10',style={'border-width': '0'}),
                    
                    html.H3('Start Year'),
                    dbc.Col(
                        dcc.Dropdown(
                        id='dd-start_year',
                        options=[
                            {'label': 2000, 'value': 2000},
                            {'label': 2001, 'value': 2001},
                            {'label': 2002, 'value': 2002},
                            {'label': 2003, 'value': 2003},
                            {'label': 2004, 'value': 2004},
                            {'label': 2005, 'value': 2005},
                            {'label': 2006, 'value': 2006},
                            {'label': 2007, 'value': 2007},
                            {'label': 2008, 'value': 2008},
                            {'label': 2009, 'value': 2009}
                        ],
                        value=2000,
                        style=dict(width='70%',
                                verticalAlign="middle"
                                )
                        ), ),

                    html.H3('End Year'),
                    dbc.Col(
                        dcc.Dropdown(
                        id='dd-end_year',
                        options=[
                            {'label': 2001, 'value': 2001},
                            {'label': 2002, 'value': 2002},
                            {'label': 2003, 'value': 2003},
                            {'label': 2004, 'value': 2004},
                            {'label': 2005, 'value': 2005},
                            {'label': 2006, 'value': 2006},
                            {'label': 2007, 'value': 2007},
                            {'label': 2008, 'value': 2008},
                            {'label': 2009, 'value': 2009},
                            {'label': 2010, 'value': 2010}
                        ],
                        value=2001,
                        style=dict(width='70%',
                            verticalAlign="middle"
                            )
                        ), ),

                    html.H3('Value'),
                    dbc.Col(
                        dcc.Dropdown(
                        id='dd-value',
                        options=[
                            {'label': 'Rate', 'value': 'rate'},
                            {'label': 'Count', 'value': 'count'}
                        ],
                        value='rate',
                        style=dict(width='70%',
                            verticalAlign="middle")
                        ),
                        # Just to add some space
                     html.Iframe(height='200', width='10',style={'border-width': '0'})
                    )
                ]
    )
])   


#LAYOUT
app.layout = html.Div([ 
    ### Add Tabs to the top of the page
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Job Growth Across Industries', value='tab-1'),
        dcc.Tab(label='Unemployment Over years', value='tab-2'),
        dcc.Tab(label='Seasonal Unemployment', value='tab-3'), 
    ]),
    html.Div([header]),
    html.Div(id='tabs-content')
            
]
)   

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs-example', 'value')])
              
def render_content(tab):
    if tab == 'tab-1':
        return content
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-3':
        pass


    
@app.callback(
    dash.dependencies.Output('plot', 'srcDoc'),
    [dash.dependencies.Input('dd-start_year', 'value'),
     dash.dependencies.Input('dd-end_year', 'value'),
     dash.dependencies.Input('dd-value', 'value'),])
def update_plot(start_year, end_year, value):

    updated_plot = make_plot(start_year, end_year, value).to_html()

    return updated_plot

if __name__ == '__main__':
    app.run_server(debug=True)