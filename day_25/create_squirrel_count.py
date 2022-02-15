import pandas

census_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_counter: int = 0
red_counter: int = 0
black_counter: int = 0

for data in census_data['Primary Fur Color']:
    if data == 'Gray':
        grey_counter += 1
    elif data == 'Cinnamon':
        red_counter += 1
    elif data == "Black":
        black_counter += 1

color_dict: dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_counter, red_counter, black_counter]
}
color_data_frame = pandas.DataFrame(color_dict)
color_data_frame.to_csv('color_count.csv')
