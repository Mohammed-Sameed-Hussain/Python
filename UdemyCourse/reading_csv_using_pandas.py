import pandas
weather_data = pandas.read_csv("weather_data.csv")
print(weather_data)
print(weather_data["temp"])