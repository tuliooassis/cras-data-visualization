import pandas as pd
import glob

class Dataset:
	def __init__(self, add_codes = False):
		allMonths = pd.DataFrame()
		firstTime = True

		# for filename in glob.glob("./Data/CRAS/Pessoas/*.csv"):
		for filename in ['./Data/CRAS/Pessoas/data_set_pessoas_cadunico_042022.csv']:
			print('Reading ', filename)

			# Read column names from file
			cols = list(pd.read_csv(filename, sep=';', nrows =1))
			print(cols)
			data = pd.read_csv(filename, sep=';', usecols =[i for i in cols if i != 'DATA_NASCIMENTO']) #, encoding='latin-1')

			if firstTime:
				allMonths = data
				firstTime = False
			else:
				allMonths = allMonths.append(data, ignore_index=True)


		print('Finished')
		self.data = allMonths

		self.data["MES_ANO_REFERENCIA"] = pd.to_datetime(self.data["MES_ANO_REFERENCIA"], format='%d/%m/%Y')
		self.data["MES_ANO_REFERENCIA"] = self.data["MES_ANO_REFERENCIA"].dt.strftime('%Y-%m')

		## Remove unused collumns
		#self.data.drop(columns=['VAL_REMUNERACAO_MES_PASSADO'], inplace=True)

		if add_codes:
			self.__add_attributes_code()

		print(self.data.columns)

	def get(self):
		return self.data
	
	def get_histogram_cols(self):
		cols_to_use = ['PARENTESCO_RF', 'IDADE', 'SEXO', 'AUXILIO_BRASIL',
       'POP_RUA', 'GRAU_INSTRUCAO', 'COR_RACA',
       'FAIXA_RENDA_FAMILIAR_PER_CAPITA',
       'CRAS', 'REGIONAL', 'FAIXA_DESATUALICACAO_CADASTRAL']
		return self.data[cols_to_use]

	def get_by_date(self, date):
		return self.data[self.data['MES_ANO_REFERENCIA'] == date]

	def get_available_dates(self):
		return self.data['MES_ANO_REFERENCIA'].unique()

	def get_date_by_index(self, index):
		return self.get_available_dates()[index]

	def __add_attributes_code(self):
		self.data.SEXO = pd.Categorical(self.data.SEXO)
		self.data['SEXO_CAT'] = self.data.SEXO.cat.codes

		self.data.PARENTESCO_RF = pd.Categorical(self.data.PARENTESCO_RF)
		self.data['PARENTESCO_RF_CAT'] = self.data.PARENTESCO_RF.cat.codes

		# self.data.AUXILIO_BRASIL = pd.Categorical(self.data.AUXILIO_BRASIL)
		# self.data['AUXILIO_BRASIL_CAT'] = self.data.AUXILIO_BRASIL.cat.codes

		self.data.GRAU_INSTRUCAO = pd.Categorical(self.data.GRAU_INSTRUCAO)
		self.data['GRAU_INSTRUCAO_CAT'] = self.data.GRAU_INSTRUCAO.cat.codes

		self.data.COR_RACA = pd.Categorical(self.data.COR_RACA)
		self.data['COR_RACA_CAT'] = self.data.COR_RACA.cat.codes

		self.data.FAIXA_RENDA_FAMILIAR_PER_CAPITA = pd.Categorical(self.data.FAIXA_RENDA_FAMILIAR_PER_CAPITA)
		self.data['FAIXA_RENDA_FAMILIAR_PER_CAPITA_CAT'] = self.data.FAIXA_RENDA_FAMILIAR_PER_CAPITA.cat.codes

		self.data.CRAS = pd.Categorical(self.data.CRAS)
		self.data['CRAS_CAT'] = self.data.CRAS.cat.codes

		self.data.REGIONAL = pd.Categorical(self.data.REGIONAL)
		self.data['REGIONAL_CAT'] = self.data.REGIONAL.cat.codes

		self.data.FAIXA_DESATUALICACAO_CADASTRAL = pd.Categorical(self.data.FAIXA_DESATUALICACAO_CADASTRAL)
		self.data['FAIXA_DESATUALICACAO_CADASTRAL_CAT'] = self.data.FAIXA_DESATUALICACAO_CADASTRAL.cat.codes
