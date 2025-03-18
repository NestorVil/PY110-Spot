# P:
#   Input: A string that is a sentence
#   Output: A boolean value dependent on if the string is a pangram
#   Explicit:
#       A panagram is a sentence that contains every single letter of the alphabet at least once
#       Should ignore numbers and punctuations
# E:
    # panagram?("The quick brown fox jumps over the lazy dog.") # should return True
    # panagram?("This is not a pangram.") # should return False
# D: 
#   Maybe sets?
# A:
#   1. Create an empty string
#   2. Go over the input_string, adding on characters to the empty string
#   3. Create a new set
#   4. Create another set that consists of the alphabet
#   5. Go over the new empty string
#   6. For each character in the new empty string, add it to the set
#   7. Compare the two sets to equality and return it

def panagram(string):
    alphabet = set(list("abcdefghijklmnopqrstuvwxyz"))
    new_string = ""
    for chara in string:
        if chara.isalpha():
            new_string += chara.lower()

    comparison_set = set(list(new_string))
    print(comparison_set == alphabet)

panagram("The quick brown fox jumps over the lazy dog.") # should return True
panagram("This is not a pangram.") # should return False