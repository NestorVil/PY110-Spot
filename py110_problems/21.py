# P:
#   Input: a list of lists, consisting of 0s and a 1
#   Ouput: A list acting as the cordinates for where the 1 is located
#   Explicit:
#       Will be a list of lists: [[0, 0, 0] [1, 0, 0]] Here its [1, 0]
#       Need to iterate through nested lists
# E:
    # #mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
    # mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) # should return [1, 1]
    # mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) # should return [2, 1]
    # mine_location([[1, 0], [0, 0]]) # should return [0, 0]
    # mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
    # mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) # should return [2, 2]
# D:
#   A way to iterate through nested lists and keep track of them
# A:
#   1. Create a new list returning_list
#   2. Go over the range of the length of the input_list
#   3. If a 1 exists in one of the lists, keep track of where, add it to the returning list, and break
#   4. Going over the nested list of where the 1 is, find where a 1 appears again and extend it to the returning_list

def mine_location(nested_lists):
    returning_list = []
    for idx in range(len(nested_lists)):
        if 1 in nested_lists[idx]:
            key_index = idx
            returning_list.append(key_index)
            break
    
    for idx in range(len(nested_lists[key_index])):
        if nested_lists[key_index][idx] == 1:
            second_key = idx
            returning_list.append(second_key)
            break

    print(returning_list) 

mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) # should return [1, 1]
mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) # should return [2, 1]
mine_location([[1, 0], [0, 0]]) # should return [0, 0]
mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) # should return [0, 0]
mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) # should return [2, 2]