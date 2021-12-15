from prettytable import PrettyTable

pokedex = PrettyTable()
print(pokedex)
pokemon_list: list = [
    {
        'name': 'Pikachu',
        'type': 'Electric'
    },
    {
        'name': 'Squirtle',
        'type': 'Water'
    },
    {
        'name': 'Charmander',
        'type': 'Fire'
    }
]
pokedex.field_names = ['Pokemon Name', 'Type']
for pokemon in range(len(pokemon_list)):
    pokedex.add_row([pokemon_list[pokemon]['name'], pokemon_list[pokemon]['type']])

pokedex.align = 'l'
print(pokedex)
