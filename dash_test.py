import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
from urllib.request import urlopen
import json
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



#start the app
app = dash.Dash(__name__)

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)
scope = ['North Carolina']
df = pd.read_csv(r"C:\Users\MG\Desktop\dash_viz\noaa.csv")

df_new = df[df['state'].isin(scope)]

df2 = pd.read_csv(r"C:\Users\MG\Desktop\dash_viz\noaa_counties.csv")



values = df_new['Total Flight Days'].tolist()



#places = df_new['name'].tolist()


#fips = df2['fips'].tolist()
#places = df2['name'].tolist()


#a = '{"label" :'
#b = '"'
#for i in range(len(places)):
 #   print(a + b + str(places[i]) + b + ', "value":' + str(fips[i]) + '},')

    #{'label': 'Alamance", "value":37001},
#groupyby = we only want these columns & and we want to get the mean of the column pct of colonies impacted
#df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()

#reset to line up the index
#df.reset_index(inplace=True)
#print(df[:5])

# ------------------------------------------------------------------------------
# App layout
#what goes inside the app layout are the dash components - graphs, dropdowns, checkboxes, sliders etc. And any html we need in here

app.layout = html.Div([

    #title page
    html.H1("Flight & Cluster Map", style={'text-align': 'center'}),

    #dcc = dash core component - with parameters below
    dcc.Dropdown(id="slct_plce",
                 options=[{"label" :"Alamance", "value":37001},
{"label" :"Alexander", "value":37003},
{"label" :"Alleghany", "value":37005},
{"label" :"Anson", "value":37007},
{"label" :"Ashe", "value":37009},
{"label" :"Avery", "value":37011},
{"label" :"Beaufort", "value":37013},
{"label" :"Bertie", "value":37015},
{"label" :"Bladen", "value":37017},
{"label" :"Brunswick", "value":37019},
{"label" :"Buncombe", "value":37021},
{"label" :"Burke", "value":37023},
{"label" :"Cabarrus", "value":37025},
{"label" :"Caldwell", "value":37027},
{"label" :"Camden", "value":37029},
{"label" :"Carteret", "value":37031},
{"label" :"Caswell", "value":37033},
{"label" :"Catawba", "value":37035},
{"label" :"Chatham", "value":37037},
{"label" :"Cherokee", "value":37039},
{"label" :"Chowan", "value":37041},
{"label" :"Clay", "value":37043},
{"label" :"Cleveland", "value":37045},
{"label" :"Columbus", "value":37047},
{"label" :"Craven", "value":37049},
{"label" :"Cumberland", "value":37051},
{"label" :"Currituck", "value":37053},
{"label" :"Dare", "value":37055},
{"label" :"Davidson", "value":37057},
{"label" :"Davie", "value":37059},
{"label" :"Duplin", "value":37061},
{"label" :"Durham", "value":37063},
{"label" :"Edgecombe", "value":37065},
{"label" :"Forsyth", "value":37067},
{"label" :"Franklin", "value":37069},
{"label" :"Gaston", "value":37071},
{"label" :"Gates", "value":37073},
{"label" :"Graham", "value":37075},
{"label" :"Granville", "value":37077},
{"label" :"Greene", "value":37079},
{"label" :"Guilford", "value":37081},
{"label" :"Halifax", "value":37083},
{"label" :"Harnett", "value":37085},
{"label" :"Haywood", "value":37087},
{"label" :"Henderson", "value":37089},
{"label" :"Hertford", "value":37091},
{"label" :"Hoke", "value":37093},
{"label" :"Hyde", "value":37095},
{"label" :"Iredell", "value":37097},
{"label" :"Jackson", "value":37099},
{"label" :"Johnston", "value":37101},
{"label" :"Jones", "value":37103},
{"label" :"Lee", "value":37105},
{"label" :"Lenoir", "value":37107},
{"label" :"Lincoln", "value":37109},
{"label" :"McDowell", "value":37111},
{"label" :"Macon", "value":37113},
{"label" :"Madison", "value":37115},
{"label" :"Martin", "value":37117},
{"label" :"Mecklenburg", "value":37119},
{"label" :"Mitchell", "value":37121},
{"label" :"Montgomery", "value":37123},
{"label" :"Moore", "value":37125},
{"label" :"Nash", "value":37127},
{"label" :"New Hanover", "value":37129},
{"label" :"Northampton", "value":37131},
{"label" :"Onslow", "value":37133},
{"label" :"Orange", "value":37135},
{"label" :"Pamlico", "value":37137},
{"label" :"Pasquotank", "value":37139},
{"label" :"Pender", "value":37141},
{"label" :"Perquimans", "value":37143},
{"label" :"Person", "value":37145},
{"label" :"Pitt", "value":37147},
{"label" :"Polk", "value":37149},
{"label" :"Randolph", "value":37151},
{"label" :"Richmond", "value":37153},
{"label" :"Robeson", "value":37155},
{"label" :"Rockingham", "value":37157},
{"label" :"Rowan", "value":37159},
{"label" :"Rutherford", "value":37161},
{"label" :"Sampson", "value":37163},
{"label" :"Scotland", "value":37165},
{"label" :"Stanly", "value":37167},
{"label" :"Stokes", "value":37169},
{"label" :"Surry", "value":37171},
{"label" :"Swain", "value":37173},
{"label" :"Transylvania", "value":37175},
{"label" :"Tyrrell", "value":37177},
{"label" :"Union", "value":37179},
{"label" :"Vance", "value":37181},
{"label" :"Wake", "value":37183},
{"label" :"Warren", "value":37185},
{"label" :"Washington", "value":37187},
{"label" :"Watauga", "value":37189},
{"label" :"Wayne", "value":37191},
{"label" :"Wilkes", "value":37193},
{"label" :"Wilson", "value":37195},
{"label" :"Yadkin", "value":37197},
{"label" :"Yancey", "value":37199}

                 ],
                     multi=False,
                     #default value
                     value=2015,
                     style={'width': "69%", 'padding': '0px 0px 0px 20px'}
                 ),
    html.Br(),

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].max(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'}),




    #children = whatever objects created below, ex: 'container'

    #space between div and graph
    html.Br(),

    #2ND thing we are returning is the fig, which refers to the figure here


    html.Div([
        dcc.Graph(id='my_bee_map', figure={}),
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Br(),


    html.Div([
        dcc.Graph(id='linechart', figure={}),],style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})

    #html.Br()




])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

    #output is the we want to output infor into our output container and our bee map
    Output(component_id='my_bee_map', component_property='figure'),
     # input for user selecting year
    [Input(component_id='crossfilter-year--slider', component_property='value')
    ]
)

#under each call back we will have to place a function
#each input needs 1 arg
#whichever option the user selected (ex 2015) will go in the option slcted argument. Argument always refers to the input
def update_graph(option_slctd):


    #creating an object to display


    # we want to make a copy of the df because we don't want to play around with the original inside the function, only play around with a copy
    dff = df.copy()
    #filter df by the option (year) the user selected, default is 2015

    dff = dff[dff["year"] == option_slctd]
    #dff = dff[dff['fips']== place_slctd]

    #Additional filtering, here we are saying that despite what the user enters, we only want rows where bees are affected by varroa

    #dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    # after figure is ready, then we just return it
    #fig = px.choropleth(
     #   data_frame=dff,
      #  locationmode='USA-states',
       # locations='fips',
        #scope="usa",
        #color='Total Flight Days',
        #hover_data=['fips', 'Total Flight Days'],
        #color_continuous_scale=px.colors.sequential.YlOrRd,
        #labels={'Total Flight Days': 'Accumulated Flight Days'},
        #template='plotly_dark'
    #)

    fig = px.choropleth(dff, geojson=counties, locations='fips',
                           color='Total Flight Days',
                           #color='Elevation (M)',
                           color_continuous_scale="Viridis",
                           range_color=(200, 300),
                           #range_color=(-200, 1000),
                           scope="usa",
                           labels={'Total Flight Days':'Total Flight Days'})

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


@app.callback(

    #output is the we want to output infor into our output container and our bee map
    Output(component_id= 'linechart', component_property='figure'),

     # input for user selecting year
    [Input(component_id='slct_plce', component_property='value')
    ]
)

def update_line_graph(plce_slctd):

    dff = df.copy()
    #filter df by the option (year) the user selected, default is 2015

    dff = dff[dff["fips"] == plce_slctd]

    bar_chart = px.bar(
            data_frame=dff,
            x='year',
            y='Total Flight Days',
            color='Total Flight Days',
            labels={'countriesAndTerritories':'Countries', 'dateRep':'date'},
            )
    bar_chart.update_layout(uirevision='foo')

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return bar_chart


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)


