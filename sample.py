from utils import data_loader
from utils.export import export_csv

def export_capital_stations():
    """
    수도권 지하철 노선도 CSV로 배포 예제
    """
    stations = data_loader.load('capital')
    export_csv(stations, filepath='./테스트.csv', encoding='utf-8')


# import csv, json
# from collections import defaultdict
# from nogada import capitalStationGraph
#
# def make():
# 	file_path = './dataset/capital/station_coordinate.csv'
# 	station_dict = defaultdict(
# 		lambda: {
# 			"lines": [],
# 			'latitude': None,
# 			'longitude': None,
# 			'around_stations': [],
# 			'version': "1.0.0"
# 		}
# 	)
#
# 	with open(file_path, 'r', encoding='utf-8') as f:
# 		reader = list(csv.reader(f))[1:]
# 		for item in reader:
# 			line, name, _, lat, lng = item
# 			station_dict[name]['lines'].append(line)
# 			station_dict[name]['latitude'] = float(lat)
# 			station_dict[name]['longitude'] = float(lng)
# 			station_dict[name]['around_stations'] = capitalStationGraph[name]
#
# 	docs = []
# 	for name, value in station_dict.items():
# 		doc = {
# 			'name': name,
# 			**value
# 		}
# 		docs.append(doc)
#
# 	docs_string = json.dumps(docs, indent='\t', ensure_ascii=False)
# 	with open("./dataset/capitalStations.json", "w", encoding='UTF-8-sig') as f:
# 		f.write(docs_string)
#
# def load():
# 	with open("./dataset/capitalStations.json", "r", encoding='UTF-8-sig') as f:
# 		a = json.load(f)
# 		print(a[:3])
#
# make()
# load()