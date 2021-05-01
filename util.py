import csv, json
from collections import defaultdict


file_path = './dataset/capital/station_coordinate.csv'
station_dict = defaultdict(lambda: {"lines":[], 'lat': None, 'lng': None})

with open(file_path, 'r') as f:
	reader = list(csv.reader(f))[1:]
	for item in reader:
		line, name, lat, lng = item
		station_dict[name]['lines'].append(line)
		station_dict[name]['latitude'] = lat
		station_dict[name]['longitude'] = lng

		