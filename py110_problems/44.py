# P:
#   Input: Two arguments (should be lists)
#   Output: A boolean value, dependingg on if the two input lists have the 'same' elements with the same multicplicities
#   Rules:
#       Same means that the elements in the lst2 are the elements in lst1 squared, regardless of the order
#       It's possible for one of the inputs to be empty or not a list. (Return False if that happens)
#       Square each element in lst1 and check if each new number exists in lst2 
#       Order does not matter 
#       11 squared -> 121 and then check if 121 is in the 2nd lst
#       Will have to square each element first, then iterate over the new numbers, and check if each number is in the 2nd lst
# E:
    # p comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True
    # p comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False
    # p comp(None, [1, 2, 3]) == False
    # p comp([1, 2], []) == False
    # p comp([1, 2], [1, 4, 4]) == False
# D:
#   Since order does not matter (can use sets??)
#   Maybe a list comprehension as a way of squaring every number
#   A way to check for membership, so maybe either in, or maybe sets
# A:
#   If the first lst is not a list or if both lists arent the same length, return False
#   Create a 'squared_nums' variable and have it be every number in the first lst squared
#   Turn 'squared_nums' into a set, turn the 2nd list into a set, and return if the two are the same

def comp(lst1, lst2):
    if not lst1 or len(lst1) != len(lst2):
        return False

    
    squared_nums = {num**2 for num in lst1}

    return squared_nums == set(lst2)

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)