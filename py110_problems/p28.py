# P:
#   Input: A string
#   Output: A list, consisting of the string splut into pairs of two characters
#   Explicit:
#       If the string contains an odd number of characters, replace the missing character of the final pair
#       with an underscore("_")
# E:
    # p solution('abc') == ['ab', 'c_']
    # p solution('abcdef') == ['ab', 'cd', 'ef']
    # p solution("abcdef") == ["ab", "cd", "ef"]
    # p solution("abcdefg") == ["ab", "cd", "ef", "g_"]
    # p solution("") == []
# D:
#   Lists and strings
# A:
#   1. Make a empty_list grouped_strings
#   2. Make an empty string "by_2"
#   3. Go over the input_string
#   4. If the length of by_2 is less than 2, add the current character to by_2
#   5. If the length of by_2 is exactly 2, add it to grouped_strings and make by_2 empty
#   6. If we reached the end of the string, add by_2 to grouped_string with an underscore
#   7. Return grouped_strings

def solution(input_string):
    result = []

    if len(input_string) % 2 != 0:
        input_string += "_"  

    for idx in range(0, len(input_string), 2):
      result.append(input_string[idx: idx + 2])

    print(result)

solution('abc') == ['ab', 'c_']
solution('abcdef') == ['ab', 'cd', 'ef']
solution("abcdef") == ["ab", "cd", "ef"]
solution("abcdefg") == ["ab", "cd", "ef", "g_"]
solution("") == []