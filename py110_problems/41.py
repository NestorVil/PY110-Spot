def duplicate_count(input_str):
    set_ = set(input_str.lower())
    input_str = input_str.lower()

    count = 0

    for chara in set_:
        if input_str.count(chara) > 1:
            count += 1
    
    return count

print(duplicate_count("") == 0)
print(duplicate_count("abcde") == 0)
print(duplicate_count("abcdeaa") == 1)
print(duplicate_count("abcdeaB") == 2)
print(duplicate_count("Indivisibilities") == 2)