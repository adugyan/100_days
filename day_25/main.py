import csv
import pandas

"""with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperature: int = []
    for row in data:
        exclusion = row[1]
        break

    for row in data:
        if row != exclusion:
            print(row[1])
            temperature.append(int(row[1]))
print(temperature)"""

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()

temp_list = data['temp'].to_list()

#read data in columns
#print(data["temp"])
# or data.temp

avg_temp = data['temp'].mean()
max_temp = data['temp'].max()
print(f"The average temperature is {avg_temp} and max is {max_temp}")

# Get Data in Row
#print(data[data['temp'] == max_temp]) # row that has the max temp is printed

monday = data[data['day'] == "Monday"]
monday_weather_C = float(monday.temp)
print('_' * 50)
F_degrees_over_C_degrees = float(9/5)
C_to_F_conversion_rate = float(32)
monday_weather_F = (monday_weather_C * F_degrees_over_C_degrees) + C_to_F_conversion_rate

#print(f"The weather in Farenheit is {monday_weather_F}. Weather in Celcius is {monday_weather_C}")

# Create dataframe from scratch
data_dict = {
    "students": ['Amy', 'Zulu', 'Joel'],
    "scores": [76, 56, 65]
}
pandas_data = pandas.DataFrame(data_dict)
print(pandas_data)
pandas_data.to_csv("new_data.csv")