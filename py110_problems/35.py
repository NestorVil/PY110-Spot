# P:
#   Input: An integer
#   Output: An integer, representing the maximum number that can be obtained by deleting exactly one digit from the input
#   Rules:
#       Deleting one digit from the input
#       Checking if the rest of the number is the maximum
#       152 -> (52, 12, 15) Then get the max from whats in the sequence
#       152 -> 52. If 52 is bigger than 0 Make it the biggest. 12. If 12 is bigger than biggest make it biggest
# E:
    # p delete_digit(152) == 52
    # p delete_digit(1001) == 101
    # p delete_digit(10) == 1
# D:
#   A possibility is to use some sort of sequence. To place every possible substring that has 1 character removed []
#   Maybe checking if one number is bigger than what happens to be the biggest number then. So comparsions
#   Working with digits, gonna have to pop one number from it, maybe turn it into a list?
# A:
#   Create a variable "possible_substrings" and make it an empty list
#   Until explicitly broken
#       For the entire range of the 'input_numbers'
#       Create a variable called 'listed_input' and have it be a list of the input digits (as strings)
        #   Remove the first element of 'listed_input'
        #       Combine the remaining of 'listed_input', turn it into a number, and palce it in 'possible_substrings'
        # Break out of this loop
#   Find the max of 'possible_substrings' and return it

def delete_digit(input_numbers):
    possible_substrings = []

    while True:
        for idx in range(len(str(input_numbers))):
            listed_input = list(str(input_numbers))

            listed_input.pop(idx)

            listed_input = "".join(listed_input)

            possible_substrings.append(int(listed_input))
        
        break

    print(max(possible_substrings))

delete_digit(152) == 52
delete_digit(1001) == 101
delete_digit(10) == 1