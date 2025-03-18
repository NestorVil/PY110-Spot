# P:
#   Input: A string
#   Output: A string, starting with #, all words starting with a capital letter, if output is longer than 140 return false
#           if the input or output is an empty string return false
#   Explicit:
#       Retyrb "False" if the input is empty, return "False" if the input or output is longer than 140 characters
#       Output must start with a hashtag
#       Every word in the hashtag has to be capitalized and stuck together
# E:
    # generate_hashtag("")                       # should return `False`
    # generate_hashtag(" " * 200)                # should return `False`
    # generate_hashtag("Do We have A Hashtag")   # should return "#DoWeHaveAHashtag"
    # generate_hashtag("Nice To Meet You")       # should return "#NiceToMeetYou"
    # generate_hashtag("this is a test")         # should return "#ThisIsATest"
    # generate_hashtag("this is a very long string" + " " * 140 + "end")  # should return "#ThisIsAVeryLongStringEnd"
    # generate_hashtag("a" * 139)                # should return "#A" + "a" * 138
    # generate_hashtag("a" * 140)                # should return `False`
# D:
#   Working with strings
# A:
#   1. If the input is empty or greater than 140 characters, return False
#   2. Split the string by a space
#   3. Create returning_string and set it to a hashtag
#   4. Going over the split_string, capitalize each word, then join them together
#   5. Add the joined string to returning string
#   6. If the returning_string is greater than 140, return False, else return the string

def generate_hashtag(string):
    if not string or len(string) > 140:
        return "False"
    
    capitalized_string = "#" + "".join(word.capitalize() for word in string.split(' '))

    if len(capitalized_string) > 140:
        return "False"
    else:
        return capitalized_string
    

generate_hashtag("")                       # should return `False`
generate_hashtag(" " * 200)                # should return `False`
generate_hashtag("Do We have A Hashtag")   # should return "#DoWeHaveAHashtag"
generate_hashtag("Nice To Meet You")       # should return "#NiceToMeetYou"
generate_hashtag("this is a test")         # should return "#ThisIsATest"
generate_hashtag("this is a very long string" + " " * 140 + "end")  # should return "#ThisIsAVeryLongStringEnd"
generate_hashtag("a" * 139)                # should return "#A" + "a" * 138
generate_hashtag("a" * 140)                # should return `False`