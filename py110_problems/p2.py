# P:
#   Input: A list of integers
#   Output: A number, which is the count of number of pairs in the list
#   Explicit:
#       A pair is defined as two equal integers separated by some other integers
#       Need a way to count digits but only once
# E:
    # pairs([1, 2, 5, 6, 5, 2]) --> 2
    # pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) --> 4
# List's wont be empty
# D:
#   Maybe sets?
# A:
#   1. Create "tracker" set
#   2. Go over the input list
#   3. Create a "count" variable and set it to 0
#   3. If the current element is already in the set, increase "count" by 1, if it isn't, add it to the set
#   4. Return "count" variable

def pairs(list1):
    tracker = set()
    count = 0
    for number in list1:
        if number in tracker:
            count += 1
        tracker.add(number)

    return count

print(pairs([1, 2, 5, 6, 5, 2]))