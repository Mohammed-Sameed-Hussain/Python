import pandas

weather_data = pandas.read_csv("weather_data.csv")

weather_dict = weather_data.to_dict()

print(weather_dict)

temp_list = weather_data["temp"].to_list()
print(temp_list)

print(weather_data["temp"].mean())
print(weather_data["temp"].max())

# Get Data in Columns
print(weather_data.condition)

# Get Data in Row
print(weather_data[weather_data.day == "Monday"])

# Getting the row having the highest temperature

print(weather_data[weather_data.temp == weather_data.temp.max()])
#
#

monday = weather_data[weather_data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
print(monday_temp )
