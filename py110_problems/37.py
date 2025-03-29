# P:
#   Input: A string
#   Output: A string. Containing only '(' and/or ')'
#   Rules:
#       Ignore capitalization
#       Iterate over the input string
#       If the character of that current iteration occurs only once, add a '('
#       If the character of that current iteration occurs more than once, add a ')'
# E:
    # p duplicate_encode("din") == "((("
    # p duplicate_encode("recede") == "()()()"
    # p duplicate_encode("Success") == ")())())"
    # p duplicate_encode("(( @") == "))(("
# D:
#   Working with strings, so need a way to keep track track of if a character appears more than once
#   A way to add characters to strings, (concatenation)
# A:
#   Create a variable called 'returning_str'
#   Iterate over the input_str
#   For each iteration, count how many times that character appears in the str
#       If it appears only once add a forward parenth
#       If it appears more than ocne add a back parent
#   Populate returning_str with every character that is the result of the iteration
#   Join returning_str and return it

def duplicate_encode(input_str):
    input_str = input_str.lower()

    returning_str = ['(' if input_str.count(chara) == 1 else ')' for chara in input_str]

    return "".join(returning_str)

duplicate_encode("din") == "((("
duplicate_encode("recede") == "()()()"
duplicate_encode("Success") == ")())())"
duplicate_encode("(( @") == "))(("