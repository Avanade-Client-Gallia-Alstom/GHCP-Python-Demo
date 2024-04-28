import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv('train_maintainance_data.csv')
columns = df.columns

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Train Maintenance Booking Form'),
    html.Div([
        html.Label(column) for column in columns
    ]),
    html.Div([
        dcc.Input(id=column, type='text', placeholder=f'Enter {column}') 
        for column in columns
    ]),
    html.Button('Submit', id='submit-button', n_clicks=0),
    
    html.Div(id='output-container')
])

@app.callback(
    Output('output-container', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State(column, 'value') for column in columns]
)
def update_output(n_clicks, *args):
    if n_clicks > 0:
        return ', '.join(f'{column}: {value}' for column, value in zip(columns, args))
    
if __name__ == '__main__':
    app.run_server(debug=True)


    