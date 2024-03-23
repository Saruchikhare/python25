n = int(input("Enter the Starting Number "))

n1,n2 = 0,1
count = 0

if n <= 0:
    print("Kindly enter a positive number")
elif n == 1:
    print("Fibonacci Sequence Answer is", n)
else:
    print("Fibonnaci Sequence Answer is")
while count < n:
    print(n1)
    nth = n1+n2
    n1,n2 = n2,nth
    count+=1

