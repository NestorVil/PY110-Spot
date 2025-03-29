# P:
#   Input: A string of digits
#   Output: A number, representing the greatest product of five consecutive digits in the given string
#   Rules:
#       Get every possible 5 consecutive digits in the input string
#       "123834539327238239583" -> ['12383', 45393', ....]
#       Splitting strings by five
#       First character + 5, second character + 5 until thats not possible anymore
#       Multiply each substring by every individual character in said substrings, and then find the max of that
# E:
    # p greatest_product("123834539327238239583") == 3240
    # p greatest_product("395831238345393272382") == 3240
    # p greatest_product("92494737828244222221111111532909999") == 5292
    # p greatest_product("92494737828244222221111111532909999") == 5292
    # p greatest_product("02494037820244202221011110532909999") == 0
# D:
#   I'm working with strings, can use string slicing to get every possible 5 consecutive characters (list comprh?)[idx:idx+5]
#   Working with strings, but returning an integer, so will need to coerce a string into a number
#   Finding the max of something, and placing substrings into a new list
# A:
#   Create a 'possible_substring' variable and populate it with every possible 5 consecutive digits
#   Multiply every number of every string in 'possible_substrings' and place it in a new variable
#       Iterate over 'possible_substrings'
#       Create a 'checker' variable and make it equal to 1
#       For every digit in every word of 'possible_substrings'
#           Multiply it (as an int) to 'checker'
#       Append 'checker' is to 'answer_possibilities'
#   Find the max in 'answer_possibilities' and return it

def greatest_product(input_str):
    possible_subtrings = [input_str[idx: idx + 5] 
                          for idx in range(len(input_str)) 
                          if len(input_str[idx: idx + 5]) == 5]

    answer_possibilities = []

    for substring in possible_subtrings:
        checker = 1

        for num in substring:
            checker *= int(num)
        
        answer_possibilities.append(checker)
    
    return max(answer_possibilities)


print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)
