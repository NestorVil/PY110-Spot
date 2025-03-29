# P:
#   Input: Any array
#   Output: A dictionary or None (if the input is empty or also None). The dictionary must contain as keys the unique
#           values of the array, and as values the counting of each value
#   Rules: If the input is falsy, return None
#       Otherwise return a dictionary, counting the amount of times a certain element appears in the input list
# E
    # p group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1}
    # p group_and_count([]) == None
    # p group_and_count(None) == None
    # p group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1}
# D:
#   Working with dictionaries, can use own methods for this like .get and adding by one
# A:
#   If the input_list is falsy, return None
#   Create a 'returning_dictionary' variable and set it to an empty dictionary
#   Iterate over 'input_list'
#   Over each iteration, make the key if it doesnt already exist, and if it does, add one and place it in returning_dictionary
#   Return returning_dictionary

def group_and_count(input_list):
    if not input_list:
        return None
    
    returning_dictionary = dict()

    for element in input_list:
        returning_dictionary[element] = returning_dictionary.get(element, 0) + 1
    
    return returning_dictionary

print(group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1})
print(group_and_count([]) == None)
print(group_and_count(None) == None)
print(group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1})