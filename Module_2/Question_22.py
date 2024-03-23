def get_first_and_last_2_chars(input_string):
    if len(input_string) < 2:
        return ''
    
    first_2_chars = input_string[:2]
    last_2_chars = input_string[-2:]

    result_string = first_2_chars + last_2_chars

    print(result_string)

input_string = input("Enter a word: ")
result = get_first_and_last_2_chars(input_string)
print("Result", result)
