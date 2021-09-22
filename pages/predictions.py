# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from joblib import load
pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app


print('LOL')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('##### Carat'), 
        dcc.Slider(
            id='carat', 
            min=0.1, 
            max=5.5, 
            step=0.1, 
            value=1, 
            marks={n: str(n) for n in range(0, 6, 1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Cut'), 
        dcc.Dropdown(
            id='cut', 
            options = [
                {'label': 'Ideal', 'value': 'Ideal'}, 
                {'label': 'Premium ', 'value': 'Premium '}, 
                {'label': 'Very Good', 'value': 'Very Good'}, 
                {'label': 'Good', 'value': 'Good'}, 
                {'label': 'Fair', 'value': 'Fair'}, 
            ], 
            value = 'Very Good', 
            className='mb-5', 
        ), 

        dcc.Markdown('##### Color of the diamond (D - the best and J - the worst)'), 
        dcc.Dropdown(
            id='color', 
            options = [
                {'label': 'D', 'value': 'D'}, 
                {'label': 'E', 'value': 'E'}, 
                {'label': 'F', 'value': 'F'}, 
                {'label': 'G', 'value': 'G'}, 
                {'label': 'H', 'value': 'H'},
                {'label': 'I', 'value': 'I'},
                {'label': 'J', 'value': 'J'}, 
            ], 
            value = 'G', 
            className='mb-5', 
        ), 

        dcc.Markdown('##### Clarity (a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)))'), 
        dcc.Dropdown(
            id='clarity', 
            options = [
                {'label': 'I1', 'value': 'I1'}, 
                {'label': 'SI2', 'value': 'SI2'}, 
                {'label': 'SI1', 'value': 'SI1'}, 
                {'label': 'VS2', 'value': 'VS2'}, 
                {'label': 'VS1', 'value': 'VS1'}, 
                {'label': 'VVS2', 'value': 'VVS2'},
                {'label': 'VVS1', 'value': 'VVS1'},
                {'label': 'IF', 'value': 'IF'},
                
            ], 
            value = 'VS2', 
            className='mb-5', 
        ),
    ],
    md=5,
)

column2 = dbc.Col(
    [


        dcc.Markdown('##### Depth % (the height of a diamond, measured from the culet to the table, divided by its average girdle diameter)'), 
        dcc.Slider(
            id='depth', 
            min=43.0, 
            max=79.0, 
            step=1, 
            value=62, 
            marks={n: str(n) for n in range(40, 80, 5)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Table % (the width of the diamond`s table expressed as a percentage of its average diameter)'), 
        dcc.Slider(
            id='table', 
            min=40, 
            max=100, 
            step=1, 
            value=56, 
            marks={n: str(n) for n in range(40, 100, 5)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Length in mm '), 
        dcc.Slider(
            id='length', 
            min=0, 
            max=11, 
            step=0.2, 
            value=4, 
            marks={n: str(n) for n in range(0, 11, 1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Width in mm'), 
        dcc.Slider(
            id='width', 
            min=0, 
            max=59, 
            step=0.5, 
            value=4, 
            marks={n: str(n) for n in range(0, 59, 5)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('##### Depth in mm'), 
        dcc.Slider(
            id='depth_mm', 
            min=0, 
            max=32, 
            step=0.2, 
            value=3, 
            marks={n: str(n) for n in range(0, 35, 5)}, 
            className='mb-5', 
        ), 
 
        html.H2('Diamod Price', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
 
    ],
    md=7,
)
@app.callback(
    Output('prediction-content', 'children'),
    [Input('carat', 'value'), Input('cut', 'value'), Input('color', 'value'), Input('clarity', 'value'), Input('depth', 'value'), Input('table', 'value'), Input('length', 'value'), Input('width', 'value'), Input('depth_mm', 'value')]
)
def predict(carat, cut, color, clarity, depth, table, length, width, depth_mm):
    # print(carat, cut, color, clarity, depth, table, length, width, depth_mm)

    
    df = pd.DataFrame(
        columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'length', 'width', 'depth_mm' ], 
        data=[[carat, cut, color, clarity, depth, table, length, width, depth_mm]]
    )
    print(df)
    y_pred = pipeline.predict(df)[0]
    print(y_pred)
    return '$' + str(y_pred)

layout = dbc.Row([column1, column2])