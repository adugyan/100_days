import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}


def generate_spelling():
    word = input("What word do you want to spell out? >").upper()
    try:
        letters: list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry. This program only takes letters\n")
        generate_spelling()
    else:
        print(letters)

generate_spelling()
