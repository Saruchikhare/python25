#4  Write a Python function to get the largest number, smallest num and sum of all from a list.  

l = [2,-4,-8,9,11]
l.sort()
print(l)

#   To find maximum number
print("Maximum Number is: ", l[-1])

#   To find minimum number
print("Minimun Number is: ", l[0])

#   To find sum of all numbers
def sum_of_list():
    total_sum = sum(l)
    return total_sum

result = sum_of_list()
print("Sum of all numbers in list is", result)