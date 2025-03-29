# P:
#   Input: A string containing different 'words' separated by spaces
#   Output: A string, with certain words reversed and combined
#   Rules:
#       If more than one word: reverse each word and combine first iwth second, third with fourth, ect
#       If there's an odd number of words: the last one stays alone, but has to be reversed too
#       Repeat ^ these processes until there's only one word without spaces
#       Return the result

#   Combining words in a string: [firstwordsecondword, thirdwordfourthword, fifthwordsixth...]
#   If there's an odd number of words, have the last word stay at the end, but reversed as well
#   Do the exact same thing again, and again... until there's only one word left
# E:
    # p reverse_and_combine_text("abc def") == "cbafed"
    # p reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi"
    # p reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed"
    # p reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
    # "trzwqfdstrteettr45hh4325543544hjhjh21lllll"
    # p reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf"
# D:
#       Working with strings and having to reverse/combine strings together
#           String splicing, alongside the join and split methods
#       A way to keep track of how many elements there are so (maybe turn strings into lists, and finding len)
#       A continious loop, maybe a while for loop
# A:
#   Create a 'split_string' variable and set it to the input_string but separated by a space
#   Find the length of 'split_string' and set it to 'length'
#   Iterate through 'split_string' while keeping track of the current index
#       For each word in 'split_string' create a new word 'reversed_word' and place it back in position
#   Join 'split_string' back together, but only the first two words, and the next two words ect, 
#       If odd, leave it alone (keep the entire string as an array)
#           Create a new_variable called 'new_string' and set it to an empty string
#           Iterate over split_string again
#           Concatenate every 2 words together and place each into new_string
#
#   Repeat this process until the length of the array is equal to one


def reversing_string(split_string):
    for idx, word in enumerate(split_string):
        new_word = word[::-1]
        split_string[idx] = new_word
    
    return split_string

def joining_string(split_string):
    retuning_list = []

    new_string = ''

    for idx, word in enumerate(split_string):
        if idx % 2 == 0 :
            new_string += word
        elif idx % 2 == 1:
            new_string += word
            retuning_list.append(new_string)
            new_string = ''
        
        if idx == len(split_string) - 1 and len(split_string) % 2 == 1:
            retuning_list.append(new_string)
        
    return retuning_list

def reverse_and_combine_text(input_string):
    split_string = input_string.split(' ')

    if len(split_string) == 1:
        return "".join(split_string)

    while True:
        split_string = reversing_string(split_string)

        split_string = joining_string(split_string)

        if len(split_string) == 1:
            return ''.join(split_string)

print(reverse_and_combine_text("abc def") == "cbafed")
print(reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi")
print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed")
print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
"trzwqfdstrteettr45hh4325543544hjhjh21lllll")
print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")