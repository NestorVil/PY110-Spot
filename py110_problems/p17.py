# P:
#   Input: A number
#   Output: Returning that number as a string in expanded form
#   Explicit:
#       12 -> "10 + 2"
#       40 -> "40 + 2"
#       70304 -> "70000" + "300" + "4"
# E:
    # expanded_form(12) # should return '10 + 2'
    # expanded_form(42) # should return '40 + 2'
    # expanded_form(70304) # should return '70000 + 300 + 4'
# D:
#   1. Need to turn numbers into strings
# A:
#   1. Turn the number into a string
#   2. For the index and character of the length of the string
#   3. Add the character and zeros equal to the remaining length of the string, adding it to a new list
#   4. Join the list by a space and a plus
#   5. Return it

def expanded_form(number):
    number_string = str(number)
    replacement_string = ""
    new_list = []

    for idx, character in enumerate(number_string):
        replacement_string += character + "0" * len(number_string[idx + 1:])
        new_list.append(replacement_string)
        replacement_string = ""

    new_list = [element for element in new_list if int(element) > 0]

    return " + ".join(new_list)


expanded_form(12) # should return '10 + 2'
expanded_form(42) # should return '40 + 2'
expanded_form(70304) # should return '70000 + 300 + 4'