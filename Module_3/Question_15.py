#15 Write a Python program to get unique values from a list.
l = [1,3,5,6,2,3,5]
l1 = []

for i in l:
    if i not in l1:
        l1.append(i)

print(l1)