# P:
#   Input: A lowercase string
#   Output: Returning a number, representing the longest substring that consists entirely of vowels
#   Explicit:
#       Returning a number
#       Longest record of vowels
# E:
    # solve("roadwarriors") # should return 2
    # solve("suoidea") # should return 3
# D:
#   A string and returning a number
# A:
#   1. Create "tracker" variable and set it to an empty string
#   2. Create a "tracker_list" variable and set it to an empty list
#   3. Go over the input string
#   4. If the character is a vowel, add it to the "tracker" variable
#   5. If the character is not a vowel, put the length of the tracker variable to the tracker_list and set tracker
#      an empty string
#   6. Return the max number of tracker_list

def solve(string):
    VOWELS = "aeiou"
    tracker = ""
    tracker_list = []
    for character in string:
        if character in VOWELS:
            tracker += character
        else:
            tracker_list.append(len(tracker))
            tracker = ""

    return max(tracker_list)

print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3