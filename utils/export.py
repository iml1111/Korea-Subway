import csv


def export_csv(stations, filepath='./export.csv', encoding='utf-8'):
    with open(filepath, 'w', newline='', encoding=encoding) as f:
        writer = csv.writer(f)
        writer.writerow(['역명', '호선', '위도', '경도'])
        for station in stations:
            for line in station['lines']:
                writer.writerow([
                    station['name'],
                    line,
                    station['latitude'],
                    station['longitude'],
                ])