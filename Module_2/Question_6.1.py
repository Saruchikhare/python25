def swap_without_temp(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

num1 = 29
num2 = 56

print("Before swap", num1, num2)
num1, num2 = swap_without_temp(num1,num2)
print("After swapping", num1, num2)