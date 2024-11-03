import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_f_dict = {letter: code for (letter, code) in df.iterrows()}

word = input("Your word: ")
word_list = [letter.upper() for letter in word]

result = [code.code for let in word_list for (letter, code) in nato_f_dict.items() if let == code.letter]
print(result)
