# P:
#   Input: Two strings
#   Output: A number signifying the number of times the 2nd string appreas in the first string
#   Explicit:
#       Need a way to count the amount of times the 2nd string appears in the first
# E:
    # solution('abcdeb','b') # should return 2 since 'b' shows up twice
    # solution('aaabbbcccc', 'bbb') # should return 1
# D:
#   Strings and numbers
# A:
#   1. Check the amount of times the 2nd string appears in the first
#   2. Assign it to a variable and return it

def solution(full_string, substring):
    return full_string.count(substring)

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1