#3  Differentiate between append () and extend () methods?

"""Append () is used to add a single variable in the already established list."""
l = [100,56,-25,69,-1]

def to_append():
    l.append(54)
    return l

result = to_append()
print("New list generated", result)

"""Extend () is used to add multiple variables in an already established list. Most preferably another list."""

l1 = [99,-34,78]

def to_extend():
    l.extend(l1)
    return l

result = to_extend()
print("Extended List is as follows: ", result)