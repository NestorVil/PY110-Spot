# P:
#   Input: Two lists of equal length
#   Output: A number, representing the absolute value of each member in each array by their correspending index squared, added together,
#               and divided by the length of one of the lists
#   Explicit:
#       The two lists will always be equal size
#       Need to get the absolute difference of each corresponding element
#       Need to square that 
#       Need to save it somewhere and add it together
#       Need to divide that sum by the length of one of the lists
# E:
# [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1] --> 1 because (1 + 1) / 2

    # p solution([1, 2, 3], [4, 5, 6]) == 9
    # p solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5
    # p solution([-1, 0], [0, -1]) == 1
# D:
#   Lists, sum, abs  function
# A:
#   1. For the idx, value of the first list
#   2. Subtract the value and the corresponding value of the 2nd list
#   3. Get the absolute value of that, then square it
#   4. Append it to a new list
#   5. Repeat steps 2-4 for the duration of the length of the list
#   6. Get the sum of that list and divide it by the length of one of the lists, then return it

def solution(list1, list2):
    squared_difference = [abs(value - list2[key])**2 for key, value in enumerate(list1)]
    sum_of_values = sum(squared_difference)
    return sum_of_values / len(list1)


solution([1, 2, 3], [4, 5, 6]) == 9
solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5
solution([-1, 0], [0, -1]) == 1