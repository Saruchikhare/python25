#21 Write a Python function to reverses a string if its length is a multiple of 4.

my_string = "Hello World Its good to see you again:-3"

s = (len(my_string))
print(s)
if (s%4==0):
    print(my_string[::-1])

else:
    print(my_string)