from dash import Dash, html, dcc
from CoordenadasParalelas import CoordenadasParalelas
from PequenosMultiplos import PequenosMultiplos
from Histograma import Histograma
from Dataset import Dataset

app = Dash(__name__)

dataset = Dataset()

app.layout = html.Div([

    html.Div(children=[
        html.H1('Pessoas Inscritas no Centro Regional de Assistência Social (CRAS) de Belo Horizonte'),
    ],
        style={'flex': 3, 'flex-basis': '100%'}),

    html.Hr(),

    html.Div(children=[
        dcc.Slider(
            id='date-selection',
            step=None,
            marks={index: element for index, element in enumerate(list(dataset.get_available_dates()))},
        ),
    ],
        style={'flex': 3, 'flex-basis': '100%'}),

    html.Div(children=[
        CoordenadasParalelas(dataset).get(app)
    ],
        style={'flex': 3, 'flex-basis': '100%'}),

    html.Div(children=[
        Histograma(dataset, 'IDADE', 'Idade').get(app),
    ], style={'flex': 1}),

    html.Div(children=[
        PequenosMultiplos(dataset, 'IDADE', 'Idade').get(app),
    ], style={'flex': 1}),

], style={'display': 'flex', 'flex-direction': 'row', 'flex-wrap': 'wrap'})

if __name__ == '__main__':
    app.run_server(debug=True)
