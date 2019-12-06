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

def make_plot1(year_range=[2003,2005], stat = 'rate'): #Add in a default value to start with


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
    df = df_raw.pivot(index = 'industry', columns = 'year', values = 'total').reset_index()

    new_df = pd.DataFrame(df["industry"])
    if stat == "rate":
        new_df["rate"] = round((df[year_range[1]] - df[year_range[0]]) / df[year_range[0]], 2)
        cb = alt.Chart(new_df).mark_bar(size = 2).encode(
                    alt.X("rate:Q", title = "Percentage Change", 
                          axis = alt.Axis(tickCount=10, format = '%')),
                    alt.Y("industry:O", title = ''),
                    color = alt.condition(alt.datum.rate > 0, alt.value("forestgreen"), alt.value("red")),
                    tooltip = ["rate"])
        cp = alt.Chart(new_df).mark_point(size = 70, filled = True, opacity = 1).encode(
                    alt.X("rate:Q", title = "Percentage Change",
                          axis = alt.Axis(tickCount=10, format = '%')),
                    alt.Y("industry:O", title = ''),
                    color = alt.condition(alt.datum.rate > 0, alt.value("forestgreen"), alt.value("red")),
                    tooltip = ["rate"])
        
    if stat == "count":
        new_df["count"] = round(df[year_range[1]] - df[year_range[0]])
        cb = alt.Chart(new_df).mark_bar(size = 2).encode(
                    alt.X("count:Q", title = "Absolute Change"),
                    alt.Y("industry:O", title = ''),
                    color = alt.condition(alt.datum.count > 0, alt.value("forestgreen"), alt.value("red")),
                    tooltip = ["count"])
        cp = alt.Chart(new_df).mark_point(size = 70, filled = True, opacity = 1).encode(
                    alt.X("count:Q", title = "Absolute Change"),
                    alt.Y("industry:O", title = ''),
                    color = alt.condition(alt.datum.count > 0, alt.value("forestgreen"), alt.value("red")),
                    tooltip = ["count"])

    return (cb + cp).properties(
        width = 575,
        height = 450
    )
def make_plot2(industries = ["Agriculture", "Construction"], stat = "rate"): #Add in a default value to start with


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
                    "height": 500, 
                    "width": 1000
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
    new_df = df_raw
    new_df = new_df.query('industry in @industries')
    new_df = new_df.loc[:, ['year', 'industry', stat]]
    
    if stat == "rate":
        cl = alt.Chart(new_df).mark_line(size = 2).encode(
                    alt.X("year:O", axis = alt.Axis(title = "Year", labelAngle = 0)),
                    alt.Y("rate:Q", axis = alt.Axis(title = "Rate", tickCount = 5, format = '%')),
                    alt.Color("industry", title = "Industry"),
                    tooltip = ["industry", "year", "rate"]).interactive()

        cp = alt.Chart(new_df).mark_point(size = 10).encode(
                    alt.X("year:O", axis = alt.Axis(title = "Year", labelAngle = 0)),
                    alt.Y("rate:Q", axis = alt.Axis(title = "Rate", tickCount = 5, format = '%')),
                    alt.Color("industry", legend = None),
                    tooltip = ["industry", "year", "rate"]).interactive()
        
    if stat == "count":
        cl = alt.Chart(new_df).mark_line(size = 2).encode(
                    alt.X("year:O", axis = alt.Axis(title = "Year", labelAngle = 0)),
                    alt.Y("count:Q", axis = alt.Axis(title = "Count")),
                    alt.Color("industry", title = "Industry"),
                    tooltip = ["industry", "year", "count"]).interactive()
        cp = alt.Chart(new_df).mark_point(size = 10).encode(
                    alt.X("year:O", axis = alt.Axis(title = "Year", labelAngle = 0)),
                    alt.Y("count:Q", axis = alt.Axis(title = "Count")),
                    alt.Color("industry", legend = None),
                    tooltip = ["industry", "year", "count"]).interactive()

    return (cl + cp).properties(
        width = 600,
        height = 450
    ).configure_legend(
        titleFontSize = 15,
        labelFontSize = 12
    )
def make_plot3(industries = ["Agriculture", "Construction"], year = 2000, stat = "rate"): #Add in a default value to start with
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
    df_raw = pd.read_csv('../data/unemply_df_month.csv', index_col=0)
    new_df = df_raw
    new_df = new_df.query('industry in @industries')
    new_df = new_df.query('year == @year')
    new_df = new_df.loc[:, ['month', 'industry', stat]]
    if stat == "rate":
        cl = alt.Chart(new_df).mark_line(size = 2).encode(
                    alt.X("month:O", axis = alt.Axis(title = "Month", labelAngle = 0)),
                    alt.Y("rate:Q", axis = alt.Axis(title = "Rate", tickCount = 5, format = '%')),
                    alt.Color("industry", title='Industry'),
                    tooltip = ["industry", "month", "rate"]).interactive()
        cp = alt.Chart(new_df).mark_point(size = 10).encode(
                    alt.X("month:O", axis = alt.Axis(title = "Month", labelAngle = 0)),
                    alt.Y("rate:Q", axis = alt.Axis(title = "Rate", tickCount = 5, format = '%')),
                    alt.Color("industry", legend = None),
                    tooltip = ["industry", "month", "rate"]).interactive()
    if stat == "count":
        cl = alt.Chart(new_df).mark_line(size = 2).encode(
                    alt.X("month:O", axis = alt.Axis(title = "Month", labelAngle = 0)),
                    alt.Y("count:Q", axis = alt.Axis(title = "Count")),
                    alt.Color("industry", title='Industry'),
                    tooltip = ["industry", "month", "count"]).interactive()
        cp = alt.Chart(new_df).mark_point(size = 10).encode(
                    alt.X("month:O", axis = alt.Axis(title = "Month", labelAngle = 0)),
                    alt.Y("count:Q", axis = alt.Axis(title = "Count")),
                    alt.Color("industry", legend = None),
                    tooltip = ["industry", "month", "count"]).interactive()
    return (cl + cp).properties(
        width = 600,
        height = 450
    ).configure_legend(
        titleFontSize = 15,
        labelFontSize = 12
    )

df_raw = pd.read_csv('../data/unemply_df_year.csv', index_col=0)
industry_options = [{'label': industry, 'value': industry} for industry in df_raw.industry.unique()]
year_options_1 = {year:str(year) for year in range(2000, 2011)}
year_options_2 = {year:str(year) for year in range(2000, 2010)}

content1 = html.Div([
                    dbc.Row([
                        dbc.Col(width = 1),
                        dbc.Col([
                            html.Br(),
                            html.Iframe(
                                sandbox='allow-scripts',
                                id='plot',
                                height='600',
                                width='900',
                                style={'border-width': '0'},
                                ################ The magic happens here
                                srcDoc=make_plot1().to_html()
                                ################ The magic happens here
                            )
                        ]),
                        dbc.Col([
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('Choose Statistic:'),
                            html.Div(
                                dcc.RadioItems(
                                    id='dd-value',
                                    options=[
                                        {'label': 'Rate', 'value': 'rate'},
                                        {'label': 'Count', 'value': 'count'}
                                    ],
                                    value='rate',
                                    style=dict(width='100%',
                                            verticalAlign="middle")
                                ),
                            ),
                            html.H4('Choose Year Range:'),
                            html.Div([
                                dcc.RangeSlider(
                                    id='year_range',
                                    count=1,
                                    min=2000,
                                    max=2010,
                                    step=1,
                                    value=[2003, 2005],
                                    marks=year_options_1
                                )
                            ], 
                            style={"display": "grid", "grid-template-columns": "90%",
                                   "text-align":"center"}
                            ),
                            html.Br(),
                            html.Div(id='year_range-output')
                        ])
                    ])
                ])
                       

content2 = html.Div([
                    dbc.Row([
                        dbc.Col(width = 1),
                        dbc.Col([
                            html.Br(),
                            html.Iframe(
                            sandbox='allow-scripts',
                            id='plot2',
                            height='600',
                            width='900',
                            style={'border-width': '0'},
                            ################ The magic happens here
                            srcDoc=make_plot2().to_html()
                            ################ The magic happens here
                            )
                        ]),
                        dbc.Col([
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('Choose Statistic:'),
                            html.Div(
                                dcc.RadioItems(
                                    id='dd-value2',
                                    options=[
                                        {'label': 'Rate', 'value': 'rate'},
                                        {'label': 'Count', 'value': 'count'}
                                    ],
                                    value='rate',
                                    style=dict(width='40%',
                                            verticalAlign="middle")
                                )
                            ),
                            html.H4('Choose Industries:'),
                            html.Div(
                                dcc.Dropdown(
                                    id='industries_list',
                                    options= industry_options,
                                    value=['Agriculture', 'Construction'],
                                    multi=True,
                                    style=dict(width='85%')
                                    
                                ),
                            )
                        ])
                    ])
                ])
             

content3 = html.Div([
                    dbc.Row([
                        dbc.Col(width = 1),
                        dbc.Col([
                            html.Br(),
                            html.Iframe(
                            sandbox='allow-scripts',
                            id='plot3',
                            height='600',
                            width='900',
                            style={'border-width': '0'},
                            ################ The magic happens here
                            srcDoc=make_plot3().to_html()
                            ################ The magic happens here
                            )
                        ]), 
                        dbc.Col([
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.H4('Choose Statistic:'),
                            html.Div(
                                dcc.RadioItems(
                                    id='dd-value3',
                                    options=[
                                        {'label': 'Rate', 'value': 'rate'},
                                        {'label': 'Count', 'value': 'count'}
                                    ],
                                    value='rate',
                                    style=dict(width='40%',
                                            verticalAlign="middle")
                                )
                            ),
                            html.H4('Choose Industries:'),
                            html.Div(
                                dcc.Dropdown(
                                    id='industries_list3',
                                    options= industry_options,
                                    value=['Agriculture', 'Construction'],
                                    multi=True,
                                    style=dict(width='85%')                                    
                                ),
                            ),
                            html.H4('Choose Year:'),
                            html.Div([
                                dcc.Slider(
                                    id='year3',
                                    min=2000,
                                    max=2009,
                                    value=2000,
                                    marks=year_options_2
                                )
                            ], 
                            style={"display": "grid", "grid-template-columns": "90%",
                                   "text-align":"center"}
                            ),
                            html.Br(),
                            html.Div(id='year3-output')
                        ])
                    ])
                ])

#LAYOUT
app.layout = html.Div([ 
    
    html.H3("Unemployment Across Industries", className="display-4"),
                html.P(
                    "These graphs display a framework for countries to examine their unemployment rates/counts across industries",
                    className="lead",
                ),
    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Job Growth Across Industries', value='tab-1'),
        dcc.Tab(label='Unemployment Throughout The Years', value='tab-2'),
        dcc.Tab(label='Seasonal Unemployment', value='tab-3'), 
    ]),
    html.Div(id='tabs-content')]
)   

#TABS FUNCTION
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs-example', 'value')])
              
def render_content(tab):
    if tab == 'tab-1':
        return content1
    elif tab == 'tab-2':
        return content2
    elif tab == 'tab-3':
        return content3


#PLOT 1 CALL BACK  
@app.callback(
    dash.dependencies.Output('plot', 'srcDoc'),
    [dash.dependencies.Input('year_range', 'value'),
     dash.dependencies.Input('dd-value', 'value'),])
def update_plot1(year_range, value):
    updated_plot1 = make_plot1(year_range, value).to_html()
    return updated_plot1

# Tab 1 chosen year range call back
@app.callback(
    dash.dependencies.Output('year_range-output', 'children'),
    [dash.dependencies.Input('year_range', 'value')])
def update_output3(year_range):
    return 'You have selected from {} to {}.'.format(year_range[0], year_range[1])

#PLOT 2 CALL BACK  
@app.callback(
    dash.dependencies.Output('plot2', 'srcDoc'),
    [dash.dependencies.Input('industries_list', 'value'),
     dash.dependencies.Input('dd-value2', 'value'),])
def update_plot2(industries, value):
    updated_plot2 = make_plot2(industries, value).to_html()
    return updated_plot2

#PLOT 3 CALL BACK  
@app.callback(
    dash.dependencies.Output('plot3', 'srcDoc'),
    [dash.dependencies.Input('industries_list3', 'value'),
     dash.dependencies.Input('year3', 'value'),
     dash.dependencies.Input('dd-value3', 'value'),])
def update_plot3(industries, year, value):
    updated_plot3 = make_plot3(industries, year, value).to_html()
    return updated_plot3

# Tab 3 chosen year call back
@app.callback(
    dash.dependencies.Output('year3-output', 'children'),
    [dash.dependencies.Input('year3', 'value')])
def update_output3(year):
    return 'You have selected year: {}'.format(year)

if __name__ == '__main__':
    app.run_server(debug=True)
