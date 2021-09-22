# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict The Diamond Price
            💎 

            Check the real Diamond price before buying it! Save money, buy smart!

            💎 


            """
        ),
        dcc.Link(dbc.Button('Diamond Price', color='primary'), href='/predictions')
    ],
    md=7,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
      html.Img(src='https://raw.githubusercontent.com/Katerynapass/New/master/580b585b2edbce24c47b23f7.png', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])