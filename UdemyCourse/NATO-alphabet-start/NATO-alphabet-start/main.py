import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
student_dict = {key[0]: key[1] for (row, key) in data.iterrows()}

print(student_dict)

word = input("Enter a word:")

word = word.upper().strip()

output_list = {letter: student_dict[letter] for letter in word}
