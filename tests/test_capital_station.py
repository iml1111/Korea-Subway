import unittest, json

FILE_PATH = "./dataset/capitalStations.json"


class CapitalStationTestCase(unittest.TestCase):

	def setUp(self):
		with open(FILE_PATH, "r", encoding='UTF-8-sig') as f:
			self.station_dict = {
				station['name']: station 
				for station in json.load(f)
			}

	def tearDown(self):
		pass

	def test_station_connection(self):
		for name, station in self.station_dict.items():
			for name_i in station['around_stations']:
				station_i = self.station_dict[name_i]
				self.assertTrue(name in station_i['around_stations'])
				self.assertTrue(name_i in station['around_stations'])
				self.assertTrue(set(station['lines']) & set(station_i['lines']))