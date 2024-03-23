def count_character(input_string):
    char_frequency={}

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

input_string = "Hello World! Nice to meet you :-)"
result = count_character(input_string) 
print(result)