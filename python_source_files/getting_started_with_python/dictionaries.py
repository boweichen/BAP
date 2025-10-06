"""
Dictionaries 
"""

#=========================================================================================================
#Dictionaries 
#=========================================================================================================
#Comma-separated list of key:value pairs
my_dict = {"Name": "Tom"}

#Dictionaries are indexed by keys
#Extracting the value given a key
print(my_dict["Name"])

#Storing a value with a key using the update method
my_dict.update({'Age': 43})
print(my_dict)

#The list function applied to a dictionary
list_keys = list(my_dict)
print(list_keys)

#The sorted function applied to a dictionary
list_keys = sorted(my_dict)
print(list_keys)

#The dict() constructor
#Takes a list of tuples
new_dict = dict([('Name', 'Amy'), ('Position', 'Data nerd')])
print(new_dict)

#Or using keyword arguments
new_dict = dict(Name = 'Amy', Position = 'Data nerd')
print(new_dict)