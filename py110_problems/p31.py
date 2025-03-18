# P:
#   Input: A string
#   Output: A word in that string, representing the highest scoring word in the string
#   Explicit:
#       A word gains score per letter. A letter's score is represented by its position in the alphabet
#       a = 1, b = 2
# E:
    # p high('man i need a taxi up to ubud') == 'taxi'
    # p high('what time are we climbing up the volcano') == 'volcano'
    # p high('take me to semynak') == 'semynak'
    # p high('aaa b') == 'aaa'
# D:
#   Dictionaries
# A:
#   1. Make a dictionary with matching points and letters
#   2. Split the input_string into multiple words by space
#   3. Go over each word, then go over each character
#   4. For each character, add the associated value from the matching dictionary to a score
#   5. Add the current index position and score to a new list, then reset score
#   6. Sort the list by the highest score then retrieve the word

def high(string):
    alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
                "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,"y": 25,"z": 26}
    
    split_string = string.split(' ')
    score = 0
    highest_score = 0

    for word in split_string:
        for chara in word:
            score += alphabet[chara]

        if score > highest_score:
            highest_score = score
            highest_word = word
        
        score = 0
    
    print(highest_word)

high('man i need a taxi up to ubud') == 'taxi'
high('what time are we climbing up the volcano') == 'volcano'
high('take me to semynak') == 'semynak'
high('aaa b') == 'aaa'
high("zzz a")

    