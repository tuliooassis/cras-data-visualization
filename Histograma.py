

import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class Histograma:
	def __init__(self, dataset, field, label):
		self.dataset = dataset
		self.date = '2021-06'
		self.field = field
		self.label = label

		self.state_id = 'state' + field

	def get(self, app):
		component = html.Div([
			html.Div([
				dcc.Dropdown(
					id=self.state_id + '-columns',
					options=list(self.dataset.get_histogram_cols().columns),
					value=self.dataset.get_histogram_cols().columns[1],
				)
			]),
			dcc.Graph(id=self.field)
		])

		@app.callback(
			Output(self.field, 'figure'),
			[Input('date-selection', 'value'),
			Input(self.state_id + '-columns', 'value')]
		)
		def update(date, column):
			self.date = self.dataset.get_date_by_index(date)
			
			fig = px.histogram(self.dataset.get_by_date(self.date), x=column)
			fig.update_layout(
				title_text='Distribuição de ' + column.title(), # title of plot
				#xaxis_title_text=self.label, # xaxis label
				yaxis_title_text='Quantidade' # yaxis label
			)
			
			return fig


		return component
