# P:
#   Input: A string of integers
#   Output: Returning a number, representing the number of substrings that result in an odd number
#           when converted to an integer
#   Explicit:
#       Splitting the string into a list of every available amount of substrings
#       Adding those substrings together
#       For each added substring check if it's odd
# E:
    # solve("1341") # should return 7
    # solve("1357") # should return 10
# D:
#   A way to create every possible substring. Indexing?
# A:
#   1. Create an empty list "substrings"
#   2. For the total range of the length of the input_string:
#       A. Add the substring leading up to the place of range to "substrings"
#       B. Add the substring starting from A idk???
#   3. For each substring in "substrings"
#       A. Convert each individual number in each substring, add them, and see if they are odd
#   4. Count the amount of odds and return the number

def subs(string):
    substrings = []
    for substring in range(1, len(string) + 1):
        substrings.append(string[:substring])
    
    return substrings


def solve(string):
    substring_list = [substring for idx in range(len(string)) for substring in subs(string[idx:])]
    full_list = [int(substring) for substring in substring_list]

    count = 0
    for numbers in full_list:
        if numbers % 2 == 1:
            count += 1
    
    return count




print(solve("1357"))
solve("1341")