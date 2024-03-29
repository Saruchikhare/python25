#7   Write a Python program to remove duplicates from a list.

l = [1,3,4,4,5,2,3]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)
