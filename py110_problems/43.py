# P:
#   Input: A positive integer written as abcd (digits in order), and a positive integer 'p'
#   Output: A number, 'k' (if it exists) so that the sum of the digits of the input_num taken to successive
#           powers of p (the 2nd number) is equal to the returning_number * input_number
#   Rules:
#       num2 = out_number * the sum of digits of num1*num2
#       (891, 1) -> First will need to split 89 into separate numbers
#           8**num2 + 9**(num2 + 1) + 1**(num2 + 2)...
#       Once I have ^, check if its equal to num1 * 

#   46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#       28 + 25 53
#   

# E:
    # p dig_pow(89, 1) == 1
    # p dig_pow(92, 1) == -1
    # p dig_pow(46288, 3) == 51
    # p dig_pow(695, 2) == 2
# D:
#   Have to split numbers in a number appart, so can turn it into a string for iteration
#   Incrementing
#   Consider using a range to find k 
# A:
#   Create the variable 'stringed_num' and have it be num1 turned into a string
#   Iterate over 'stringed_num' and have each element of it turned back into an integer, with each integer being raised to the power
#       of num2. For each successive iteration, add one to num2
#   Get the sum of 'stringed_num'
#   Over the range starting from 1, up to 100
#       Multiply 'num1' by the current range and if that equals 'stringed_num', return the range number
#   If no such number exists, return -1

def dig_pow(num1, exponent):
    stringed_num = str(num1)
    stringed_num = [int(number)**(exponent + idx)
                    for idx, number in enumerate(stringed_num)]
    

    sum_ = sum(stringed_num)

    for checker in range(1, 999):
        possible_number = checker * num1

        if possible_number > sum_:
            return -1
        
        if possible_number == sum_:
            return checker



print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)

    # for checker in range(1, 999):
    #     possible_number = checker * num1

    #     if possible_number > num1:
    #         return -1
        
    #     if possible_number == num1:
    #         return checker