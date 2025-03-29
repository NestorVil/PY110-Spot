# P:
#   Input: Two numbers
#   Output: Either 0 or 1, depending on if there is a st raight triple of a number at any place in num1 and also a straight double
#                          of the same number in num2
#   Rules:
#       Checking for consecutive numbers in both input numbers
#       For the first number, worrying about 3 consecutive numbers
#       For the second number, worrying about 2 consecutive numbers
#       They both have to be checking the same number
#       (666789, 12345667) == 1 # 3 straight 6's in num1, 2 straight 6's in num2
#       Get the first num from the first number, times it by three, and check if it's in the first number, and if thats true times it by 2 
#           and check if its in the second number
#       Move on to the next number
#       RETURNING EITHER 1 OR 0
# E:
    # p triple_double(12345, 12345) == 0
    # p triple_double(666789, 12345667) == 1 # 3 straight 6's in num1, 2 straight 6's in num2
# D
#   Working with digits, might consider turning them into strings and checking for membership when checking for consecutives
#   '666789' -> '6' * 3 which will equal '666'. And then check if that number is in the first num, and for the 2nd '6' * 2 == '66' and check 
# A:
#   Turn num1 and num2 into strings of the same name
#   Iterate over num1
#       For each iteration, multiply that character by 3 and check if its in num1
#           If it is, multiply that character by 2, and check if it's in num2
#               If both are true, return 1
#   If went over the entire iteration without returning  anything, return 0 

def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 = set(num1)

    for num in num1:
        if num * 3 in num1:
            if num * 2 in num2:
                return 1
    
    return 0

print(triple_double(666789, 12345667) == 1)
print(triple_double(12345, 12345) == 0)