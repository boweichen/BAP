"""
Types
"""

a = 7
b = -2

#Assert relationships
print(a > b)
print(a <= b)
print(a == b)
print(a != b, end = "!!!\n")

#Assign Booleans
d = False
c = (a > b)

#And, or, not
e = not d
f = not d and c
g = d or c

#Bool function: is it falsy or truthy
print(bool(0))
print(bool(118))

print(bool("word"))
print(bool(""))


