import csv

with open("weather_data.csv") as weather_data_file:
    weather_data = csv.reader(weather_data_file)
    print(weather_data)
    temperature = []
    for row in weather_data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)