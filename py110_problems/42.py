# P:
#   Input: A string (containing only letters, with uppercase letters all being unique (one of a kind))
#   Output: A string (In alphabetical order, starting from uppercase + that letter's lowercase letters, then continue again)
#   Rules:
#       Uppercase stands for one element, lowercasae stands for another element
#       Get one uppercase letter from the input_string then find all other lowercase letters from that string
#       Do so again for the next uppercase letter
#       If theres no next uppercase letter, should be good
#       Returned in alphabetical order
#       
# E:
    # p find_children("abBA") == "AaBb"
    # p find_children("AaaaaZazzz") == "AaaaaaZzzz"
    # p find_children("CbcBcbaA") == "AaBbbCcc"
    # p find_children("xXfuUuuF") == "FfUuuuXx"
    # p find_children("") == ""
# D:
#   Need a way to sort the string according to their alphabetic placement
#   A way to keep track of whats in a string, and the ability to reset
# A:
#   Create a 'sorted_string' variable and have it be the sorted input_string
#   Create a variable 'running_str' and make it an empty string
#   Create a variable 'checker_list' and make itt an empty list
#   Iterate over sorted_string
#   If the current letter iteration is capitalized
#       Add it to 'running_str'
#       Check each character over the rest of sorted_string
#       If that character is the current letter iteration but capitalized
#           Add it to 'running_str'
#       Add 'running_str' to 'checker_list' then make 'running_str' empty again
#  Over iteration, if the next character is not capitalized, break out of the iteration
#  Join 'checker_list' together, and return it

def find_children(input_str):
    sorted_string = sorted(input_str)
    running_str = ''
    checker_list = []

    for idx, chara in enumerate(sorted_string):
        if chara.isupper():
            running_str += chara
            for next_chara in sorted_string[idx:]:
                if next_chara.isupper():
                    continue
                elif next_chara.casefold() == chara.casefold():
                    running_str += next_chara
            checker_list.append(running_str)
            running_str = ""

        if chara.islower():
            break

    return "".join(checker_list)

print(find_children("abBA") == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")