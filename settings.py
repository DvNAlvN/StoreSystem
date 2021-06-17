from json import load, dump


class Settings:

	def __init__(self):

		#App Conf
		self.title = "Data Gudang"

		#Window Conf
		base = 60
		ratio =(16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]

		self.screen = f"{self.width}x{self.height}+200+75"


		#Img Conf
		self.logo = "img/logo.jpeg"


		#Dummy Contact Data

		self.item = None
		self.load_data_from_json()


	def load_data_from_json(self):
		with open("data/data.json", "r") as json_file:
			self.item = load(json_file)

	def save_data_to_json(self):
		with open("data/data.json", "w") as json_file:
			dump(self.item, json_file)






