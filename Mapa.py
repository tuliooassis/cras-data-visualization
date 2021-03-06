import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

class Mapa:
	def __init__(self, dataset):
		self.dataset = dataset

		self.crasGeolocation = {
			'CRAS PETROPOLIS': (-20.01266937619392, -44.02714971130215), 
			'ENDERECO FORA AREA CRAS': (0,0),
			'CRAS VILA SANTA RITA DE CASSIA': (-19.95361390459403, -43.94145762092032), 
			'CRAS VILA ANTENA': (-19.949003053082475, -43.96275592336323),
			'CRAS VILA MARIA': (-19.853547830257213, -43.887976225410966), 
			'CRAS CONJUNTO PAULO VI': (-19.8321987983892, -43.888453797125415), 
			'CRAS VISTA ALEGRE': (-19.953806795399366, -43.99649726980435),
			'CRAS MANTIQUEIRA': (-19.8003904075944, -43.981496240254934), 
			'CRAS INDEPENDENCIA': (-20.015840129902582, -44.028910373229834), 
			'CRAS PROVIDENCIA': (-19.85360021363596, -43.93158859831775),
			'CRAS VILA BIQUINHAS': (-19.842560662846243, -43.940305927299214), 
			'CRAS VILA CEMIG': (-19.998186559125923, -43.992718813503245), 
			'CRAS GRANJA DE FREITAS': (-19.906881922922306, -43.88348406617839),
			'CRAS CONFISCO': (-19.865401333369707, -44.018914183293695), 
			'CRAS NOVO OURO PRETO': (-19.876557940823123, -43.98802814841431),
			'CRAS VILA NOSSA SENHORA DE FATIMA': (-19.934338682389885, -43.90451211652901), 
			'CRAS VILA MARCOLA': (-19.93868205770567, -43.91175843442696),
			'CRAS VILA SAO JOSE': (-19.900168639515897, -43.99551376432711),
			'CRAS NOVO AARAO REIS   BRASILINA MARIA DE OLIVEIRA': (-19.845983155301074, -43.91473424758369),
			'CRAS JARDIM FELICIDADE': (-19.82965995833287, -43.92770558928296),
			'ENDERECO NAO GEORREFERENCIADO': (0,0),
			'CRAS HAVAI VENTOSA': (-19.963549973222538, -43.97069461151225),
			'CRAS VILA SENHOR DOS PASSOS': (-19.905853595084604, -43.948719361070744),
			'CRAS VILA SUMARE': (-19.89039481626893, -43.9644083337257),
			'CRAS APOLONIA': (-19.82863906989695, -43.98728523747388),
			'CRAS MORRO DAS PEDRAS   GRACA SABOIA': (-19.94285471144954, -43.96347212906046),
			'CRAS SANTA ROSA': (-19.881198417152522, -43.959280472727556),
			'CRAS PEDREIRA PRADO LOPES': (-19.90354994714038, -43.94728113927203),
			'CRAS ALTO VERA CRUZ': (-19.914940590785104, -43.88961988527733),
			'CRAS ARTHUR DE SA   UNIAO': (-19.88090568703948, -43.92003811953022),
			'CRAS ZILAH SPOSITO': (-19.80489370873361, -43.928082411922986),
			'CRAS TAQUARIL': (-19.920164330801484, -43.87578285894951),
			'CRAS VILA COQUEIRAL': (-19.9153969179839, -44.02439901383172),
			'CRAS MARIANO DE ABREU': (-19.895439258336282, -43.88982372289429),
			'CRAS CALIFORNIA': (-19.9174900865449, -44.009830484383805),
			'CRAS LAGOA': (-19.80958763224746, -44.00081485493766)
		}

		filteredDataset = self.dataset.get().copy()[['CRAS', 'REGIONAL', 'PARENTESCO_RF']]
		filteredDataset = filteredDataset.drop(filteredDataset[filteredDataset['REGIONAL'].isin(['ENDERECO NAO GEORREFERENCIADO', 'Endereco FORA Region'])].index)
		filteredDataset = filteredDataset.drop(filteredDataset[filteredDataset['CRAS'].isin(['ENDERECO FORA AREA CRAS', 'ENDERECO NAO GEORREFERENCIADO'])].index)

		self.crasFamiliesWithGeo = filteredDataset.groupby(['CRAS', 'REGIONAL']).count().reset_index()

		self.crasFamiliesWithGeo['lat'] = self.crasFamiliesWithGeo.apply(lambda row: self.crasGeolocation[row['CRAS']][0], axis=1)
		self.crasFamiliesWithGeo['lon'] = self.crasFamiliesWithGeo.apply(lambda row: self.crasGeolocation[row['CRAS']][1], axis=1)

		self.crasFamiliesWithGeo.rename(columns = {'PARENTESCO_RF': 'count'}, inplace = True)

	def get(self, app):
		component = html.Div([
			dcc.Graph(
				id='mapa',
				figure=px.scatter_geo(self.crasFamiliesWithGeo,
					lat="lat", lon="lon",
					color="REGIONAL",
					hover_name="CRAS", size="count",
					projection="natural earth", scope="south america",
					center={ 'lat': -19.845983155301074, 'lon': -43.91473424758369}
				)
			)
		])

		return component
