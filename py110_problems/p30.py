# P:
#   Input: Two strings (words)
#   Output: A boolean value determining if the two are anagrams
# E:
    # p is_anagram('Creative', 'Reactive') == true
    # p is_anagram("foefet", "toffee") == true
    # p is_anagram("Buckethead", "DeathCubeK") == true
    # p is_anagram("Twoo", "WooT") == true
    # p is_anagram("dumble", "bumble") == false
# D:
#   Maybe sorting and equality
# A:
#   1. Sort each character and joing them as strings. Lowercasing each first
#   2. Return if the two are equal to each other

def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    string1 = "".join(sorted(string1))
    string2 = "".join(sorted(string2))

    print(string1 == string2)
    return string1 == string2


is_anagram('Creative', 'Reactive') 
is_anagram("foefet", "toffee") 
is_anagram("Buckethead", "DeathCubeK") 
is_anagram("Twoo", "WooT") 
is_anagram("dumble", "bumble")