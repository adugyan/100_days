import os.path
PLACEHOLDER = "[name]"
save_path = 'Output/ReadyToSend/'

with open('Input/Names/invited_names.txt') as guest_names:
    names = guest_names.readlines()

with open('Input/Letters/starting_letter.txt', mode='r') as letter:
    contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as  completed_letter:
            completed_letter.write(new_letter)



