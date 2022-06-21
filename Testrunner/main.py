"""try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['sdfsdf'])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write('Something')
except KeyError as error_message:
    print(f"Key {error_message} does not exist in the dictionary")
else:
    print(file.read())
finally:
    print('No matter what persevere and intelligently work toward my goals')
    file.close()"""

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

