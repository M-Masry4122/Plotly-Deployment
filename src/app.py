from dash import html,dcc,Dash,Input,Output,State
import plotly.express as px
import pandas as pd
 
df = px.data.gapminder()

app = Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div(children = [

html.H1("Gap Minder", style={'color': 'blue', 'fontSize': 50, 'text-align': 'center', 'background-color': 'lightblue'}),
html.Div(dcc.Graph(id='myGraph')),
html.Div(dcc.Slider(id='yearSlider',min=df['year'].min(),max=df['year'].max(),step=None,value=df['year'].min(),marks={str(year): year for year in df['year'].unique()}),style={'width':'80%','margin':'auto'}),



])

@app.callback(
    Output(component_id='myGraph', component_property='figure'),
    Input(component_id='yearSlider', component_property='value')

)
def update_graph(year):
    print(year)
    new_df = df[df['year']==year]
    fig = px.scatter(data_frame=new_df,x='gdpPercap', y='lifeExp', color='continent',size='pop', size_max=60,
            hover_name='country', range_x=[50,50000], range_y=[25,90])
    return fig


app.run_server(use_reloader=True)