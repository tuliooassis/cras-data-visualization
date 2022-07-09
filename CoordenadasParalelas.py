import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class CoordenadasParalelas:
	def __init__(self, dataset):
		self.dataset = dataset
		self.date = '2021-06'

	def get(self, app):
		component = html.Div([
			dcc.Graph(id='coordenadas-paralelas')
		])

		@app.callback(
			Output('coordenadas-paralelas', 'figure'),
			Input('date-selection', 'value')
		)
		def update(date_index):
			self.date = self.dataset.get_date_by_index(date_index)
			df = self.dataset.get_by_date(self.date)

			fig = go.Figure(data=
				go.Parcoords(
					dimensions = list([
						dict(tickvals = [*range(len(df['SEXO_CAT'].unique()))],
							ticktext = df['SEXO'].unique(),
							label = 'Gênero', values = df['SEXO_CAT']),

						dict(range = [0,115],
							label = "Idade", values = df['IDADE']),

						dict(range = [0,30000],
							label = "Remuneração", values = df['VAL_REMUNERACAO_MES_PASSADO']),

						dict(tickvals = [*range(len(df['PARENTESCO_RF_CAT'].unique()))],
							ticktext = df['PARENTESCO_RF'].unique(),
							label = 'Parentesco', values = df['PARENTESCO_RF_CAT']),

						# dict(tickvals = [*range(len(df['AUXILIO_BRASIL_CAT'].unique()))],
						# 	ticktext = df['AUXILIO_BRASIL'].unique(),
						# 	label = 'Auxilio Brasil', values = df['AUXILIO_BRASIL_CAT']),

						dict(tickvals = [*range(len(df['GRAU_INSTRUCAO_CAT'].unique()))],
							ticktext = df['GRAU_INSTRUCAO'].unique(),
							label = 'Grau de Instrução', values = df['GRAU_INSTRUCAO_CAT']),

						dict(tickvals = [*range(len(df['COR_RACA_CAT'].unique()))],
							ticktext = df['COR_RACA'].unique(),
							label = 'Etnia', values = df['COR_RACA_CAT']),

						dict(tickvals = [*range(len(df['FAIXA_RENDA_FAMILIAR_PER_CAPITA_CAT'].unique()))],
							ticktext = df['FAIXA_RENDA_FAMILIAR_PER_CAPITA'].unique(),
							label = 'Renda per capita', values = df['FAIXA_RENDA_FAMILIAR_PER_CAPITA_CAT']),

						# dict(tickvals = [*range(len(df['CRAS_CAT'].unique()))],
						#	  ticktext = df['CRAS'].unique(),
						#	  label = 'CRAS', values = df['CRAS_CAT']),

						dict(tickvals = [*range(len(df['REGIONAL_CAT'].unique()))],
							ticktext = df['REGIONAL'].unique(),
							label = 'Regional', values = df['REGIONAL_CAT']),

						dict(tickvals = [*range(len(df['FAIXA_DESATUALICACAO_CADASTRAL_CAT'].unique()))],
							ticktext = df['FAIXA_DESATUALICACAO_CADASTRAL'].unique(),
							label = 'Desatualização Cadastral', values = df['FAIXA_DESATUALICACAO_CADASTRAL_CAT']),
					])
				)
			)
			return fig


		return component
