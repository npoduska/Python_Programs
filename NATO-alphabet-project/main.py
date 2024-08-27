"""Enter in a word, then it spits out the NATO alphabet phonetic spelling of the word.
    Example; "Andy" would be: "Alfa", "Nickel", "Delta", "Yankee"
    """

#These couple examples are just code samples. Not needed for the NATO alphabet program to work. 
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
alphabet_data = pandas.read_csv("NATO-alphabet-project/nato_phonetic_alphabet.csv") #Bring in the data from the CSV file.
# print(alphabet_data)


#Loop through rows of a data frame, use this just to get an idea of how iterrows works. This is not needed for the program to work.
# for (index, row) in alphabet_data.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(row.letter)
    # letter=row.letter
    # print(row.code)
    # code=row.code
    # alphabet_dict = {letter:code for (letter,code) in alphabet_data.iterrows()}
# print(alphabet_dict)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [alphabet_dict[letter] for letter in word]

print(output_list)