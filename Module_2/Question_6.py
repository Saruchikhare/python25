#6 Write python program that swap two number with temp variable and without temp variable.

"""
Temp Variable: refers to a variable used to hold intermediate values during the execution of a program or 
a specific algorithm. Temp variables are typically short-lived and may be reused or discarded once 
their purpose is served. They are commonly used for storing results of intermediate computations, 
swapping values, or facilitating certain operations.

Non Temp Variable: is a variable that holds data for longer durations or for the duration of the program's 
execution. Non-temp variables typically store important or persistent data that needs to be retained and 
accessed throughout the program's lifespan. They may represent state, configuration settings, user inputs, 
or any other data that remains relevant across multiple parts of the program."""

def swap_with_temp(a,b):

    temp = a 
    a = b
    temp = b 
    return a, b

num1 = 30
num2 = 20

print("Before Swapping:", num1, num2)
num1, num2 = swap_with_temp(num1,num2)
print("After Swapping:", num1, num2)