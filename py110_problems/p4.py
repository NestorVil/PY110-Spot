# P:
#   Input: A list of words
#   Output: A list of integers, eah integer represents the count of letters in the word that occupy
#           their position in the alphabet
#   Explicit:
#       Matching the position of a character in each substring to their correct position in the alphabet
#       Keeping track of how much that happens
#       ABCD -> ABDD A[0] B[1] D[4] so here it's 3 times
# E:
    # solve(["abode","ABc","xyzD"]) # should return [4, 3, 1]
    # solve(["abide","ABc","xyz"]) # should return [4, 3, 0]
#   # Case doesn't matter
# D:
#   Working with indexes
# A:
#   1. Create the entire alphabet "alphabet"
#   2. Create a "count" variable and set it to 0
#   3. Create a new empty list
#   3. Go over the entire list
#   4. For each word in the list
#       A. If the current index of that character (lowercase) matches the character of the matching index of alphabet
#           A. Increase "count" by 1
#       Append the count to the empty list then set count back to 0

def solve(words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    returning_list = []
    for word in words:
        for idx, chara in enumerate(word):
            if chara.lower() == alphabet[idx]:
                count += 1
        returning_list.append(count)
        count = 0
    
    return returning_list

print(solve(["abode","ABc","xyzD"]))
print(solve(["abide","ABc","xyz"]))
print(solve([]))