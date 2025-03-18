# P:
#   Input: A string, is dubstep (WUB)s
#   Output: A string, consisting of all non Wubs
#   Explicit:
#       The input consists of a single non-empty string, consisting only of uppercase
#       Remove the wubs
# E:
    # song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB") -> "WE ARE THE CHAMPIONS MY FRIEND"
# D:
#   Remove them
# A:
#   1. Split the string by WUBs
#   2. If the length of each element in the new list is greater than 0, join them
#   3. Return it

def song_decoder(string):
    returning = " ".join([word for word in string.split("WUB") if len(word) > 0])
    
    return returning

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")