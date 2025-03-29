# P:
#   Input: A list, consisting of conesuctive (increasing) letters as input
#   Output: A string, representing the missing letter in the list
#   Rules:
#       Only worrying about one case 
#       The length of the list will always be at least 2, and it will always be valid (with 1 letter missing)
#     
# E:
    # # ['a','b','c','d','f'] -> 'e'
    # # ['O','Q','R','S'] -> 'P'

    # p find_missing_letter(['a','b','c','d','f']) == 'e'
    # p find_missing_letter(['O','Q','R','S']) == 'P'
# D:
#   Working with lists, and returning a string
#   Consider using indexes to determine where in the alphabet a letter starts, and to check if
#       the next letter exists in the input_list or not
# A:
#   Create a 'lower_case' variable and set it to the alphabet but lowercase
#   Create a 'upper_case' variable and set it to the alphabet but uppercase
#   Determine if the first element of the input_list is upper or lower, and then use the appropiate alph
#   Look at the first element of 'input_list' and determine its index position in the appropiate alph
#   Look at the next element of 'input_list' and see if it comes right after the next letter in appropiate
#   If it does, go on to the next letter, and if it does not, return that letter
def lower_case(input_list):
    return 'abcdefghijklmnopqrstuvwxyz'

def upper_case(input_list):
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_missing_letter(input_list):
    if input_list[0].isupper():
        appropiate_alphabet = upper_case(input_list)
    else:
        appropiate_alphabet = lower_case(input_list)

    appropiate_index = appropiate_alphabet.index(input_list[0])

    for num in range(len(appropiate_alphabet)):
        if appropiate_alphabet[appropiate_index + num] not in input_list:
            return appropiate_alphabet[appropiate_index + num]

print(find_missing_letter(['a','b','c','d','f']) == 'e')