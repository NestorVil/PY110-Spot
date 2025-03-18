# P:
#   Input: A string
#   Output: 


def get_char_count(string):
    lowercase = string.lower()
    uniq_char = set(list(lowercase))
    uniq_char = sorted(list(uniq_char))
    returning_dict = dict()
    for char in uniq_char:
        if char.isalnum():
            key = lowercase.count(char)
            returning_dict.setdefault(key, [])
            returning_dict[key].extend(char)
    
    print(dict(sorted(returning_dict.items(), reverse=True)))
    #return dict(sorted(returning_dict.items(), reverse=True))

get_char_count("Mississippi") # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
get_char_count("Hello. Hello? HELLO!!") # should return {6: ['l'], 3: ['e', 'h', 'o']}
get_char_count("aaa...bb...c!") # should return {3: ['a'], 2: ['b'], 1: ['c']}
get_char_count("aaabbbccc") # should return {3: ['a', 'b', 'c']}
get_char_count("abc123") # should return {1: ['1', '2', '3', 'a', 'b', 'c']}