# P:
#   Input: Two dictionaries, representing a recipe and available ingredients
#   Output: A number, representing the max amount of cakes possible to make
#   Explicit:
#       If ingredients not present, return 0
#       Dividing values of matching keys 
# E:
# must return 2
    # cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2

    # # must return 11
    # cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 1700, "flour": 20000,
    # "milk": 20000, "oil": 30000, "cream": 5000}) == 11

    # # must return 0
    # cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
    # "milk": 2000}) == 0

    # # must return 0
    # cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
    # "milk": 2000, "apples": 15, "oil": 20}) == 0

    # # must return 0
    # cakes({"eggs": 4, "flour": 400},{}) == 0

    # # must return 1
    # cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1
# D:
#   Comparing the lengths of dictionaries, dividing values and keeping track of them
# A:
#   1. Return 0 if the lengths of the two dictionaries do not match
#   2. Create a max_cakes variable and set it to 0
#   3. Going over the key, value of reciple
#   4. Divide the associated value of each key by the associated ingredient value
#   5. If the result is higher than max_cakes, make max_cakes equal that
#   6. Return max_cakes

def cakes(recipe, ingredients):
    if len(recipe) > len(ingredients):
        return 0
    
    list_of_cakes = []

    for key in recipe.keys():
        possible_cakes = ingredients[key] // recipe[key]
        list_of_cakes.append(possible_cakes)
    
    return min(list_of_cakes)


# must return 2
cakes({"flour": 500, "sugar": 200, "eggs": 1},{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2

# must return 11
cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 1700, "flour": 20000,
"milk": 20000, "oil": 30000, "cream": 5000}) == 11

# must return 0
cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
"milk": 2000}) == 0

# must return 0
cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000,
"milk": 2000, "apples": 15, "oil": 20}) == 0

# must return 0
cakes({"eggs": 4, "flour": 400},{}) == 0

# must return 1
cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},{"sugar": 1, "eggs": 1, "flour": 3,
"cream": 1, "oil": 1, "milk": 1}) == 1