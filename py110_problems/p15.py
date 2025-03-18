# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the 
# opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their
# phones -- every time you press the button it sends you a list of one-letter strings representing directions 
# to walk (e.g., ['n', 's', 'w', 'e']). You always walk only a single block in a direction, and you know
#  it takes you one minute to traverse one city block. Create a function that will return `True` if the walk
#  the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, 
# return you to your starting point. Return `False` otherwise.

# Note: You will always receive a valid list containing a random assortment of direction letters 
# ('n', 's', 'e', or 'w' only). It will never give you an empty list (that's not a walk, that's standing still!).


# P:
#   Input: A list consisting of ["n", "e", "s", "w"]
#   Output: A boolean value, depending on if theres only 10 elements in the list, and if not at the destination at the start
#   Explicit:
#       Can return false if the len isn't exactly 10
#       Can return false if there isn't an equal amount 
# E:

# is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
# is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
# is_valid_walk(['w']) # should return False
# is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return F

# D:
#   A way to count, keep track of letters, and length
# A:
#   1. Return false if the length of the walk isn't 10
#   2. Initialize "at_office" variable and set it to 0
#   3. Go over the input_list
#   4. If "n", add one, if "s" subtract one, if "w" add 2, if "e" subtract 2
#   5. Return at_offce equal to 0

def is_valid_walk(directions):
    if len(directions) != 10:
        return False
    
    at_office = 0
    for direction in directions:
        match direction:
            case "n":
                at_office += 1
            case "s":
                at_office -= 1
            case "e":
                at_office += 2
            case "w":
                at_office -= 2
    
    return at_office == 0

is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) # should return True
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) # should return False
is_valid_walk(['w']) # should return False
is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) # should return F