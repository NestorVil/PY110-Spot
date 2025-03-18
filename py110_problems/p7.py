# P:
#   Input: A list of words
#   Output: A string, constructed by concetenating the nth letter from each word
#            where n is the position of the word in the list
# E:
# D:
#   Indexing for each letter in order of the list
# A:
#   1. Create an empty string variable
#   2. Go over the input list, tracking the index and element each time
#   3. Add the value at the current index to empty string
#   4. Return empty string

def nth_char(list1):
    returning_string = ""

    for idx, value in enumerate(list1):
        returning_string += value[idx]

    return "".join([value[idx] for idx, value in enumerate(list1)])
    return returning_string

print(nth_char(['yoda', 'best', 'has']))