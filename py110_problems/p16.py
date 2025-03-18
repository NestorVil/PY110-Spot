# Write a function that takes in a string of one or more words and returns the same string, 
# but with all words of five or more letters reversed. Strings passed in will consist of only 
# letters and spaces. Spaces will be included only when more than one word is present.

# P:
#   Input: A string, consisting of one or more words
#   Output: A string, with all words of five or more letters reversed
# E:
    # spin_words("Hey fellow warriors") # should return "Hey wollef sroirraw"
    # spin_words("This is a test") # should return "This is a test"
    # spin_words("This is another test") # should return "This is rehtona test"
# D:
#   Strings are immutable, lists and strings
# A:
#   1. Split the input_string into split_string
#   2. Go over each element of split_string
#   3. If the length of that element is greater than 5 letters, reverse it
#   4. Join the split_string and return it

def spin_words(string):
    split_string = string.split(" ")
    for idx, word in enumerate(split_string):
        if len(word) > 5:
            split_string[idx] = word[::-1]

    return " ".join(split_string)

spin_words("Hey fellow warriors") # should return "Hey wollef sroirraw"
spin_words("This is a test") # should return "This is a test"
spin_words("This is another test") # should return "This is rehtona test"