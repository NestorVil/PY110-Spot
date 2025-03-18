# P:
#   Input: A string, in c amel case
#   Output: A string, in kebab case
#   Explicit:
#       Kebab case is a string separated by dashes "-" when it identifies new word
#       Looking at the examples, it shouldnt even consider numbers at all (delete them)
# E:
    # kebabize('camelsHaveThreeHumps') # should return 'camels-have-three-humps'
    # kebabize('myCamelHas3Humps') # should return 'my-camel-has-humps'
# D:
#   A way to separate and join strings
# A:
#   1. Remove any non characters from the string
#   2. Create "returning_string" variable and make it an empty string
#   3. Go over the string
#   4. Add each character (lowercase) to the returning_string
#   5. If encounters a letter that is capitalize, add a dash then the letter (lowercase)
#   6. Return it

def kebabize(string):
    string = "".join([chara for chara in string if chara.isalpha()])
    returning_string = ""
    for chara in string:
        if chara == chara.lower():
            returning_string += chara
        else:
            returning_string += "-" + chara.lower()
    
    # returning_string = "".join([chara if chara == chara.lower() else "-" + chara.lower() for chara in string]) this works
    print(returning_string)



kebabize("camelsHaveThreeHumps")