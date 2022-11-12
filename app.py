# Import libraries
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load the live dataset
aqi = pd.read_csv('https://raw.githubusercontent.com/Open-Oven/AQI_scraper/main/AQI.csv')
aqi['Date']= pd.to_datetime(aqi['Date'],dayfirst=True)
# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=aqi['City'].unique(),
                            value='Delhi')

app.layout = html.Div(children=[
    html.H1(children='Air Quality Index of Indian cities Dashboard'),
    geo_dropdown,
    dcc.Graph(id='aqi-graph')
])


# Set up the callback function
@app.callback(
    Output(component_id='aqi-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_aqi = aqi[aqi['City'] == selected_geography]
    line_fig = px.line(filtered_aqi,
                       x='Date', y='Index Value',
                       title=f'Air Quality index in {selected_geography}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
