# P:
#   Input: A string, containing letters and hashtags
#   Output: A string, with every letter before a hashtag removed, and all hashtags removed
#   Rules:
#       Treat "#' like a backspace in a string (remove the letter because the #)
#       Find the index of the first hashtag, then remove the letter before that hashtag, alongside the first hashtag as well
# E:
    # p clean_string('abc#d##c') == "ac"
    # p clean_string('abc####d##c#') == ""
# D:
#   Need a way to find the index and the index - 1 of an element 
#   Working with strings (immutable) so to remove elements from it might need a list?
#   A way to check for membership, to check if a hashtag still exists in the string
# A:
#   Create a list_string variable and set it to the input_str as a list
#   Find the index of the first hashtag minus 1 and set it to current_index
#   Remove whatever character is at current_index
#   Remove the first hashtag
#   Repeat steps 2-4 so long as hashtags exist in the list_string
#   Join list_string together as a string and return it

def clean_string(input_string):
    listed_str = list(input_string)

    while True:
        if '#' in listed_str:
            if listed_str.index('#') == 0:
                listed_str.remove('#')
            else:
                relevant_index = listed_str.index('#') - 1
                listed_str.pop(relevant_index)
                listed_str.remove('#')
        else:
            break
    
    return "".join(listed_str)



print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == '')