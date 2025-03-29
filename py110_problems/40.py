# P:
#   Input: A list (of integers)
#   Output: A number, representing the minimum number to be inserted in the list so that the sum of all elements 
#           of the list should equal the closest prime number
#   Rules:
#       If the sum of the input list is already prime, return 0
#       The output can't be negative
#       Check if the sum of the input_list is prime, if it is return 0, otherwise add 1 and check again ect
#       A prime number is if only 1 * that number divides cleanly into that number. It has no other numbers
# E:
    # p minimum_number([3,1,2]) == 1
    # p minimum_number([5,2]) == 0
    # p minimum_number([1,1,1]) == 0
    # p minimum_number([2,12,8,4,6]) == 5
    # p minimum_number([50,39,49,6,17,28]) == 2
# D:
#   To check if a number is prime. Can use a range and a way to check for the remainder of a number
#   Working with lists, and returning an integer
#   A way to keep track of that integer (incremeneting)
# A:
#   Create a sum_of_list variable and set it to the sum of the input_list
#   Create a 'checker' variable and set it to 0
#   If 'sum_of_list' is already prime, return 'checker'
#       If it isn't add one to 'sum_of_list' and one to 'checker'
#   So long as 'sum_of_list' isn't prime, add one to both 'checker' and 'sum_of_list'
#   If it is prime, return 'checker'


def is_prime(sum_):
    for num in range(2, sum_):
        if sum_ % num == 0:
            return False

    return True

def minimum_number(input_list):
    sum_of_list = sum(input_list)
    checker = 0

    while True:
        if is_prime(sum_of_list) == False:
            sum_of_list += 1
            checker += 1
        else:
            return checker

print(minimum_number([3,1,2]) == 1)
print(minimum_number([5,2]) == 0)
print(minimum_number([1,1,1]) == 0)
print(minimum_number([2,12,8,4,6]) == 5)
print(minimum_number([50,39,49,6,17,28]) == 2)