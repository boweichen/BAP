"""
Tuples & Sets 
"""

#=========================================================================================================
#Tuples
#=========================================================================================================
#An empty tuple
first_tuple = ()

#Add one item to tuple using +
item_one = "First name"
item_two = "Last name"
item_three = "Position"

#Note the comma!
updated_tuple = first_tuple + (item_one, ) + (item_two, ) + (item_three, )

#Alternative approach: convert to list
updated_list = list(updated_tuple)

#Note indexing works
print(updated_tuple[0])

#As well as slicing
print(updated_tuple[:2])

#Tuples are not mutable!

#Unpacking a tuple into items and lists
first_name, *other = updated_tuple

#=========================================================================================================
#Sets
#========================================================================================================
#Empty set
first_set = set()

#Order does not matter; it does not accept duplicates

#Adding colours to a set of colours
first_set.add("red")
first_set.add("blue")
first_set.add("green")
first_set.add("red")

print(first_set)

#In and not in operator
print("red" in first_set)
print("blue" not in first_set)

#Indexing does not work as the order is not fixed
#first_set[0]