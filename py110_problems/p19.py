# A string is considered to be in title case if each word in the string is either:
# a) Capitalized (that is, only the first letter of the word is in upper case)
# b) Considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalized.

# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
# The list of minor words will be given as a string with each word separated by a space. Your function should ignore 
# the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

# P:
#   Input:
#       Two strings, the first string the title, the second string consisting of exceptions
#   Output: A string, where each word in the first string is capitalized unless a word in it exists in the 2nd string
#   Explicit:
#       First word of the first string is always titled
#       Title each word, unless it exists in the 2nd string
# E:
    # title_case('a clash of KINGS', 'a an the of') # should return 'A Clash of Kings'
    # title_case('THE WIND IN THE WILLOWS', 'The In') # should return 'The Wind in the Willows'
    # title_case('the quick brown fox') # should return 'The Quick Brown Fox'
# D:
#   Strings are immutable, can use title
# A:
#   1. Split both strings into lists
#   2. Titlize the first word of the first string
#   3. Going over each element of first_string beginning on the 2nd word
#   4. If that word exists in the 2nd string, ignore it, otherwise title it
#   5. Join the first_string together again and return it

def title_case(title, exceptions=""):
    split_title = title.split(' ')

    for idx, element in enumerate(split_title):
        if element in exceptions:
            split_title[idx] = element.lower()
        else:
            split_title[idx] = element.capitalize()

    split_title[0] = split_title[0].capitalize()

    return " ".join(split_title)

title_case('a clash of KINGS', 'a an the of') # should return 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return 'The Wind in the Willows'
title_case('the quick brown fox') # should return 'The Quick Brown Fox'