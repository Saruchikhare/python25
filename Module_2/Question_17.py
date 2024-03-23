def swap_and_combine(str1, str2):
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:1] + str2[1:]

    result = swapped_str1 +' '+ swapped_str2

    return result

string1 = input("Enter a Sentence: ")
string2 = input("Enter a Sentence: ")

result = swap_and_combine(string1,string2)
print("Result", result)