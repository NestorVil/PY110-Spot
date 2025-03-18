def scramble(str1, str2):
    if len(str2) > len(str1):
        return False

    str1_list = list(str1)
    str2_list = list(str2)

    for char in str2_list:
        if char in str1_list:
            str1_list.remove(char)
        else:
            return False
    return True


scramble('rkqodlw', 'world') # should return True
scramble('cedewaraarossoqqyt', 'carrot') # should return True
scramble('katas', 'steak') # should return False
scramble('scriptjava', 'javascript') # should return True
scramble('scriptingjava', 'javascript') # should return True