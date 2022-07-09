import pandas as pd
import glob

class Dataset:
	def __init__(self):
		self.date = {}

		allMonths = pd.DataFrame()
		firstTime = True

		# for filename in glob.glob("./Data/CRAS/Pessoas/*.csv"):
		for filename in ['./Data/CRAS/Pessoas/data_set_pessoas_cadunico_062021.csv', './Data/CRAS/Pessoas/data_set_pessoas_cadunico_052021.csv']:
			print('Reading ', filename)

			data = pd.read_csv(filename, sep=';', encoding='latin-1')

			data["MES_ANO_REFERENCIA"] = pd.to_datetime(data["MES_ANO_REFERENCIA"], format='%d/%m/%Y')
			data["MES_ANO_REFERENCIA"] = data["MES_ANO_REFERENCIA"].dt.strftime('%Y-%m')

			if firstTime:
				allMonths = data
				firstTime = False
			else:
				allMonths = allMonths.append(data, ignore_index=True)

			self.date[data['MES_ANO_REFERENCIA'].unique()[0]] = data
		print('Finished')
		self.data = allMonths
		print(self.data.columns)

	def get(self):
		return self.data

	def get_by_date(self, date):
		return self.date[date]

	def get_available_dates(self):
		return self.date.keys()

	def get_date_by_index(self, index):
		return list(self.date.keys())[index]