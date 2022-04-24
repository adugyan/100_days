import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

word = input("What word do you want to spell out? >").upper()
letters: list = [nato_dict[letter] for letter in word]

print(letters)
