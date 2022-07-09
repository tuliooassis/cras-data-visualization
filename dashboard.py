from dash import Dash, html, dcc
from CoordenadasParalelas import CoordenadasParalelas
from PequenosMultiplos import PequenosMultiplos
from Histograma import Histograma
from Dataset import Dataset

import sd_material_ui

app = Dash(__name__)

dataset = Dataset()
dataset_with_codes = Dataset(add_codes=True)

graphs = html.Div([
	html.Div(children=[
		html.H1('Pessoas Inscritas no Centro Regional de Assistência Social (CRAS) de Belo Horizonte'),
    	sd_material_ui.Divider(),
	],
		style={'flex': 3, 'flex-basis': '100%'}),

	html.Div(children=[
		dcc.Slider(
			id='date-selection',
			step=None,
			value=0,
			marks={index: element for index, element in enumerate(dataset.get_available_dates())},
		),
	],
		style={'flex': 3, 'flex-basis': '100%'}),

	html.Div(children=[
		sd_material_ui.Paper([
			CoordenadasParalelas(dataset_with_codes).get(app)
		])
	],
		style={'flex': 3, 'flex-basis': '100%'}),

	html.Div(children=[
		sd_material_ui.Paper([
			Histograma(dataset, 'IDADE', 'Idade').get(app),
		]),
	],
		style={'flex': 1}),


	html.Div(children=[
		sd_material_ui.Paper([
			PequenosMultiplos(dataset, 'IDADE', 'Idade').get(app),
		])
	], style={'flex': 1}),
], style={'display': 'flex', 'flex-direction': 'row', 'flex-wrap': 'wrap'})

app.layout = graphs

if __name__ == '__main__':
	app.run_server(debug=True)
