# P:
#   Input: A string of random letters
#   Output: A substring of the inputstring, representing the longest substring possible where the charas are in alphabetical order
#   Explicit:
#       Need to check multiple substrings
#       Need to use alphabet
# E:
    # longest('asd')                  # should return 'as'
    # longest('nab')                  # should return 'ab'
    # longest('abcdeapbcdef')         # should return 'abcde'
    # longest('asdfaaaabbbbcttavvfffffdf') # should return 'aaaabbbbctt'
    # longest('asdfbyfgiklag')        # should return 'fgikl'
    # longest('z')                    # should return 'z'
    # longest('zyba')                 # should return 'z'
# D:
#   Maybe comparison operator? And range to keep track of substrings
# A:
#   1. Create a longest_substring variable and set it to the first character of the input_string
#   2. Go over the input_string starting at the second letter
#   3. If that letter is bigger than the last added character to longest_substring, add it to that
#   4. If no characters were added, set longest_substring to the next letter and repeat 2-4
#   5. If the longest_substring is just the last letter, set_longest_substring to the first letter
#   6. Return longest substring

def longest(string):
    longest_substrings = []

    for idx in range(1, len(string) + 1):
        subtstring = string[idx - 1]

        for chara in string[idx:]:
            if chara > subtstring[-1] or chara == subtstring[-1]:
                subtstring += chara
            else:
                break
        
        longest_substrings.append(subtstring)

    print(max(longest_substrings, key=len))
    #return max(longest_substrings, key=len)



longest('asd')                  # should return 'as'
longest('nab')                  # should return 'ab'
longest('abcdeapbcdef')         # should return 'abcde'
longest('asdfaaaabbbbcttavvfffffdf') # should return 'aaaabbbbctt'
longest('asdfbyfgiklag')        # should return 'fgikl'
longest('z')                    # should return 'z'
longest('zyba')   