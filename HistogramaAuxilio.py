

import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class HistogramaAuxilio:
	def __init__(self, dataset):
		self.dataset = dataset
		self.options = ['PARENTESCO_RF', 'IDADE', 'SEXO', 'GRAU_INSTRUCAO',
			'COR_RACA', 'FAIXA_RENDA_FAMILIAR_PER_CAPITA', 'REGIONAL',
			'FAIXA_DESATUALICACAO_CADASTRAL']

	def get(self, app):
		component = html.Div([
			html.Div([
				dcc.Dropdown(
					id='histograma-auxilio-columns',
					options=self.options,
					value=self.options[1],
				)
			]),
			dcc.Graph(id='histograma-auxilio')
		])

		@app.callback(
			Output('histograma-auxilio', 'figure'),
			Input('histograma-auxilio-columns', 'value')
		)
		def update(column):

			fig = go.Figure()
			com_auxilio_brasil, sem_auxilio_brasil = self.dataset.get_auxilio()
			fig.add_trace(go.Histogram(x=com_auxilio_brasil[column], histnorm='probability', name='Recebe Auxílio Brasil'))
			fig.add_trace(go.Histogram(x=sem_auxilio_brasil[column], histnorm='probability', name='Não Recebe Auxílio Brasil'))

			# Overlay both histograms
			fig.update_layout(barmode='overlay')
			# Reduce opacity to see both histograms
			fig.update_traces(opacity=0.75)
			fig.update_layout(
				title_text='Distribuição de ' + column.title(), # title of plot
				#xaxis_title_text='Idade', # xaxis label
    			yaxis_title_text='Porcentagem', # yaxis label
    			yaxis_tickformat = '.2%'
			)
			return fig


		return component
