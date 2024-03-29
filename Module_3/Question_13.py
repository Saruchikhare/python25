#13 Write a Python program to select an item randomly from a list.
import random

l = [2,5,3,-1,7]

random_number = random.choice(l)

print("A randomly chosen number is", random_number)