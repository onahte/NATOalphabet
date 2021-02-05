#Practicing working with .csv

import pandas as pd

xcel = pd.read_csv('nato_phonetic_alphabet.csv')
alphabet = {col.letter: col.code for (index, col) in xcel.iterrows()}

name = input('What is your name: ').upper()

new_name = [alphabet[letter] for letter in name]
print(new_name)