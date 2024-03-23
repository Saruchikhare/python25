def add_ing_ly(input_string):
    if len(input_string) < 3:
        return input_string

    if input_string.endswith('ing'):
        return input_string + 'ly'
    
    return input_string + 'ing'

input_string = input("Enter a word: ")
result = add_ing_ly(input_string)
print("Result is: ", result)
