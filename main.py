# Automated letter writing with python

with open("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

with open("Input/Letters/starting_letter.txt") as start:
    starting_text = start.read()

for name in invited_names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letters:
        new_letter = starting_text.replace("[name]", name.strip())
        letters.write(new_letter)

