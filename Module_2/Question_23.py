#23 Write a Python function to insert a string in the middle of a string.

def insert_string_middle(original_string, string_to_insert):
    
    middle_index = len(original_string) // 2

  
    result_string = original_string[:middle_index] + string_to_insert + original_string[middle_index:]

    return result_string


original_string = input("Enter the original string: ")
string_to_insert = input("Enter the string to insert: ")

result = insert_string_middle(original_string, string_to_insert)
print("Result:", result)
