# P:
#   Input: A string consisting of either one way or many words
#   Output: A string, where each word has the first and last letter remaining in place, and everything between sorted alphabetically
#   Explicit:
#       Punctuation should remain at the same place as it started
#       Strings can have many wordspy


def idk(word):
    if word.isalnum():
        return word


print(sorted(idk("ou'v")))