import pandas as pd
import glob

class Dataset:
	def __init__(self):
		allMonths = pd.DataFrame()
		firstTime = True

		# for filename in glob.glob("./Data/CRAS/Pessoas/*.csv"):
		for filename in ['./Data/CRAS/Pessoas/data_set_pessoas_cadunico_042022.csv']:
			print('Reading ', filename)

			# Read column names from file
			cols = list(pd.read_csv(filename, sep=';', nrows =1))
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

	def get(self):
		return self.data
	
	def get_histogram_cols(self):
		cols_to_use = ['PARENTESCO_RF', 'IDADE', 'SEXO', 'AUXILIO_BRASIL',
			'GRAU_INSTRUCAO', 'COR_RACA',
			'FAIXA_RENDA_FAMILIAR_PER_CAPITA',
			'REGIONAL', 'FAIXA_DESATUALICACAO_CADASTRAL']
		return self.data[cols_to_use]

	def get_by_date(self, date):
		return self.data[self.data['MES_ANO_REFERENCIA'] == date]

	def get_available_dates(self):
		return self.data['MES_ANO_REFERENCIA'].unique()

	def get_date_by_index(self, index):
		return self.get_available_dates()[index]

	def get_responsaveis(self):
		return self.data[self.data['PARENTESCO_RF'] == 'PESSOA RESPONSAVEL PELA UNIDADE FAMILIAR RF']
	
	def get_auxilio(self):
		com_auxilio_brasil = self.data.loc[self.data['AUXILIO_BRASIL']=="SIM"]
		sem_auxilio_brasil = self.data.loc[self.data['AUXILIO_BRASIL']=="NAO"]
		return com_auxilio_brasil, sem_auxilio_brasil
