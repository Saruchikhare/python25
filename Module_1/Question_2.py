#2 Write a Python program to get the Factorial number of given number.

fac = 1
n = int(input("Enter a Number: "))
for i in range(1,n+1):
    fac*= i

print(fac, "is the given factorial")

