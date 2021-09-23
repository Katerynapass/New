# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
           

            ### Welcome to the Diamond Price Estimator App!

            This app was made to predict the diamond price using Machine learnng.
            You can use this app to predict the price of the diamond you want and this prediction can be very helpful in negotiating price with local retailers.

            For this app I used dataset called Diamonds. Which contains 10 columns.
                        
            **Dataset description:**
            
            **price** - price in US dollars (\$326--\$18,823)

            **carat** - weight of the diamond (0.2--5.01)

            **cut** - quality of the cut (Fair, Good, Very Good, Premium, Ideal)

            **color** - diamond colour, from J (worst) to D (best)

            **clarity** - a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))

            **depth** - total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)

            **table** - width of top of diamond relative to widest point (43--95)

            **length** - length in mm (0--10.74)

            **width** - width in mm (0--58.9)

            **depth_mm** - depth in mm (0--31.8)

            I started my work doing some EDA and then spliting my data.

            For this dataset I will predict the price of the diamond by its features. My target vector here is 'price' column, which is continuous variable so I will work with regression problem here.
            Then i used train_test_split method to split my data on training and testind subsets.

            After spliting I established baseline which is average price multiplied by length of the target.
            Baseline mean absolute error was 3036.64. So, I need to build the model which will beat this baseline.

            I built three different models to see which one is the best to make predictions.
            First model was Ridge Regression.
            Second model was Random Forest Regression.
            And last but not least was XGB Redression.

            After I checked metrics I saw that all my models beat the baseline and rigth now Random Forest model is working the best and showing good results with low mean absolute error.

            Even though results are good, I decided to make some model tuning to get even better results.
            Tuning models improved my results and it appears that XGB Regressor is showing the best results with MAE: 266.44. So I used XGB Regressor to make predictions for this app.

            While working on this project I also plotted validation curves, feature importances, partial dependency plots, and Shapley force plots.

            **If you willing to see my code you are welcome to visit my GitHub clicking on link below.**

            [Diamond Price Estimator Code](https://github.com/Katerynapass/Unit2-Project.git)





            """
        ),

    ],
)

layout = dbc.Row([column1])