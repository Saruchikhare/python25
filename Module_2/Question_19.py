def replace_not_poor(input_string):
    
    index_not = input_string.find('not')
    index_poor = input_string.find('poor')
    
    
    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        
        return input_string[:index_not] + 'good' + input_string[index_poor + 4:]
    
    
    return input_string


input_string = input("Enter a string: ")
result = replace_not_poor(input_string)
print("Result:", result)
