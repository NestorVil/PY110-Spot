# P:
#   Input: A string
#   Output: A dictionary that counts the occurances of each lowercase letter in the string. letters: count
#   Explicit:
#       Returning a dictionary
#       counting only the lowercase letters
#       
# E:
#   letter_count('launchschool') #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 }
# D:
#   Working with dictionaries and a way of counting
# A:
#   1. Create a new dictionary: returning_dictionary
#   2. Go over the input string
#   3. If a character is lower case, add it to the dictionary
#   4. If the character is already in the dictionary, increase its count
#   5. Return the dictionary

def letter_count(string):
    returning_dict = {}
    for chara in string:
        if chara.islower():
            returning_dict[chara] = returning_dict.get(chara, 0) + 1

    return returning_dict

print(letter_count('launchschool')) #=> { ’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1 }