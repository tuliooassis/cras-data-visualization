

import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class HistogramaResponsaveis:
	def __init__(self, dataset):
		self.dataset = dataset
		self.options = ['IDADE', 'SEXO', 'AUXILIO_BRASIL', 'GRAU_INSTRUCAO',
			'COR_RACA', 'FAIXA_RENDA_FAMILIAR_PER_CAPITA', 'REGIONAL',
			'FAIXA_DESATUALICACAO_CADASTRAL']

	def get(self, app):
		component = html.Div([
			html.Div([
				dcc.Dropdown(
					id='histograma-responsaveis-columns',
					options=self.options,
					value=self.options[0],
				)
			]),
			dcc.Graph(id='histograma-responsaveis')
		])

		@app.callback(
			Output('histograma-responsaveis', 'figure'),
			Input('histograma-responsaveis-columns', 'value')
		)
		def update(column):
			
			fig = px.histogram(self.dataset.get_responsaveis(), x=column)
			fig.update_layout(
				title_text='Distribuição de ' + column.title(), # title of plot
				#xaxis_title_text=self.label, # xaxis label
				yaxis_title_text='Quantidade' # yaxis label
			)
			
			return fig


		return component
