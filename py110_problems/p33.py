# P:
#   Input: A dictionary, and a list of numbers
#   Output: Keys of the dictionary if one of it's values dont match one of the numbers in the list

pockets = {
    'bob': [1],
    'tom': [2, 5],
    'jane': [7]
}

def find_suspects(suspects, allowed_itmes):
    returning_list = []
    for key, values in suspects.items():
        for value in values:
            if value not in allowed_itmes and key not in returning_list:
                returning_list.append(key)
    
    if returning_list == []:
        return None
    return returning_list


print(find_suspects(pockets, [1, 2]) == ['tom', 'jane'])
print(find_suspects(pockets, [1, 7, 5, 2]) == None)
print(find_suspects(pockets, []) == ['bob', 'tom', 'jane'])
print(find_suspects(pockets, [7]) == ['bob', 'tom'])