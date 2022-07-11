

import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class PequenosMultiplos:
	def __init__(self, dataset, field, label):
		self.dataset = dataset
		self.date = '2021-06'
		self.field = field
		self.label = label

		self.state_id = 'pequenos-multiplos-' + field

	def get(self, app):
		component = html.Div([
			html.Div([
				dcc.Dropdown(
					id=self.state_id + '-columns',
					options=list(self.dataset.get_histogram_cols().columns),
					value=self.dataset.get_histogram_cols().columns[0],
				)
			]),
			dcc.Graph(id=self.field + '1')
		])

		@app.callback(
			Output(self.field + '1', 'figure'),
			[Input('date-selection', 'value'),
			Input(self.state_id + '-columns', 'value')]
		)
		def update(date_index, column):
			self.date = self.dataset.get_date_by_index(date_index)
			
			peopleCadUnico_hist = self.dataset.get_by_date(self.date)[['REGIONAL' , column, 'COR_RACA']]
			peopleCadUnico_hist = peopleCadUnico_hist.drop(peopleCadUnico_hist[peopleCadUnico_hist['REGIONAL'].isin(['ENDERECO NAO GEORREFERENCIADO', 'Endereco FORA Region'])].index)


			fig = px.histogram(peopleCadUnico_hist, facet_col="REGIONAL", color="COR_RACA", facet_col_wrap=3)
			fig.update_layout(
				title_text='Pequenos Múltiplos por Regional', # title of plot
				xaxis_title_text='Idade', # xaxis label
				yaxis_title_text='Quantidade', # yaxis label
			)

			
			return fig


		return component
