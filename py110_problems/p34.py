# P:
#   Input: A string
#   Output: A list consisting of the input_string, which the associated index letter capitalized
# E:
    # p wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    # p wave("") == []
    # p wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    # p wave(" gap ") == [" Gap ", " gAp ", " gaP "]
# D:
#   A way to keep track of index locations
# A:
#   1. Split the input_string into split_string
#   2. For each individual word
#   3. Keep track of the character and index per iteration per word
#   4. Capitalize the associated letter by the current index spot, and add each to a list
#   5. Repeat step 2-4 for the next word and add them together

def word(word):
    new_list = []
    for idx, chara in enumerate(word):
        if word[idx] != " ":
            temp = list(word)
            temp[idx] = chara.upper()
            new_list.append("".join(temp))
    print(str(new_list))
    return str(new_list)



word("two words")