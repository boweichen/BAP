"""
Lists
"""

#========================================================================================================
#Lists
#========================================================================================================
#Empty list
empty = [] #alternative list()

#Add item to list
a = 7
b = 8
c = -2
d = "fun"

#Append method and dot operator
empty.append(a)
empty.append(b)
empty.append(c)
empty.append(d)

#The len function
#Shows number of items stored in list
len(empty)

#Indexing
print(empty[0])

#To get the last entry
print(empty[-1])

#Alternative
print(empty[len(empty) - 1])

#Remove one item
empty.pop(-1) 

#Check return value
#It modifies the list empty

#Slicing
print(empty[0 : 1]) #start (inclusive) to end (exclusive)
print(empty[0 : 2]) 
print(empty[: 2])
print(empty[1 :])

#Steps (third entry; default is 1)
print(empty[0 :: 2]) 

#Shallow copy
copy = empty[:] 

#Reverse order; mutable
copy.reverse()

#The in and not in operator
print(d in empty)
print(d not in empty)







