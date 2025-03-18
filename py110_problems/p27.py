# P:
#   Input: A string, and a list of strings, the string representing a word, and the list hosting possible annagrams
#   Output: A list of strings, where each string is a possible annagram from the input_string
#   Explicit:
#       An anagram is if two words contain the same letters
#       Compare if each string in the list has the exact letters as the input_string
# E:
    # p anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    # p anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    # p anagrams('laser', ['lazing', 'lazy', 'lacer']) == []
# D:
#   Anagrams have to have t he same characters so that can help
# A:
#   1. Going over the words in the input_list, going over the characters in each word, if a character doesnt
#       exist in the input_string, don't consider it, put the rest in a new list
#   2. Sort the input_string, and sort each word in the new list
#   3. Going over the new list, if its qual to the sorted_input_string add it to a newer list
#   4. Return newer list

def anagrams(string, possible_anagrams):
    precise_list = possible_anagrams[:]

    for words in possible_anagrams:
        for chara in words:
            if chara not in string:
                precise_list.remove(words)
                break

    return [word for word in precise_list if sorted(word) == sorted(string)]
    


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy', 'lacer']) == []