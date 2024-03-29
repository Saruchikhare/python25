#2  How will you remove last object from a list? 
def remove_last_object():
    l = [1,-2,3,4,6]
    l.pop()
    return l

result = remove_last_object()
print(result)


#2.1    Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
def reverse_list():
    list1 = [2,33,222,14,25]
    reversed_list = list1[::-1]
    return reversed_list

result = reverse_list()
print(result)