# P:
#   Input: A string of text
#   Output: A list, consisting of the top 3 most occuring words in descending order of the number of occurances
#   Explicit:
#       A word is a string of letters that may contain one or more apostrophes
#       Matches should be case sensitive
#       Ties may be broken arbitrarily
#       If a text contains fewer than 3 equal words, then either the top-2 or top-1 words should be returned
#       Return an empty list if a text contains no words

#       A way to keep track of a word if it appears more than once
# E:
# D:
# A:
#   1. Creat an empty dictionary "tracker"
#   2. Split the input string by a space
#   3. Check each word in the split_string
#       A. Check each character of each word
#           A. If a character not a letter or doesn't have an apostrophe, don't consider it
#       B. Append the new character to a new list
#   4. Go over the new list
#   5. For each word in the new list, add the word and its length to a dictionary
#   6. Sort the dictionary in descending order by its value and return the keys

def top_3_words(string):
    tracker = {}
    split_string = string.split(" ")
    new_list = []
    for word in split_string:
        tracker[word] = tracker.get(word, 0) + 1
    
    sorted(tracker.items(), key=tracker.values())


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))