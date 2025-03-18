# P:
#   Input: A number
#   Output: A number, representing its multiplicative persistence
#   Explicit:
#       Multiplicative persistence is the number of times you must multiply the digits in num until you reach a single digit
#       Ex: 39 -> Return 3 because 3 * 9 = 27, 2 * 7 = 14, 1 * 4 = 44

#       A way to keep track of each multiplication 
# E:
    # persistence(39) # should return 3, because 3*9=27, 2*7=14, 1*4=4
    # # and 4 has only one digit
    # persistence(999) # should return 4, because 9*9*9=729, 7*2*9=126,
    # # 1*2*6=12, and finally 1*2=2
    # persistence(4) # should return 0, because 4 is already a one-digit number
    # persistence(25) # should return 2, because 2*5=10, and 1*0=0
# D:
#   I think there's a way to use recursive functions here but I'm scared to use them
#   Can use a while statement instead
# A:
#   1. Set a "tracker" variable to 0
#   2. Convert the input_number to a string
#   3. If the length of the string is 1, return tracker
#   4. While True:
#       A. Add one to tracker variable
#       B. Create a new inner_tracker variable and set it to 1
#       C. Going over the input_number (making sure to convert each element to an int):
#       D. Multiply it to inner_tracker
#       E. If inner_tracker is greater than the length of 1, break
#   5. Return tracker

def persistence(number):
    tracker = 0
    input_number = str(number)

    if len(input_number) == 1:
        return tracker
    
    while True:
        tracker += 1
        inner_tracker = 1

        for element in str(input_number):
            inner_tracker *= int(element)

        input_number = inner_tracker
    
        if len(str(input_number)) == 1:
            break

    return tracker

persistence(39) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit
persistence(999) # should return 4, because 9*9*9=729, 7*2*9=126,
# 1*2*6=12, and finally 1*2=2
persistence(4) # should return 0, because 4 is already a one-digit number
persistence(25) # should return 2, because 2*5=10, and 1*0=0