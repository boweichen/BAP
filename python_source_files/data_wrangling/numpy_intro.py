"""
NumPy
"""
#Importing a library or module

import numpy as np

#Operations with numerics
a = 7
b = 2

#Square root
print(np.sqrt(a))

#Creating Numpy array
#Similar to list - but only numerics
vector = np.zeros(5) #Column vector

#The all one vector
ones = np.ones(5)

#Change entries in vector
vector[0] = a
vector[-1] = b

#Or assign array as follows
vector_a = np.array([1, 2, 34, 7])

#Operations on vectors
#Vectorization is much faster 
sqrt_vector = np.sqrt(vector)

#Create a matrix 
matrix = np.zeros((3, 4)) #first integer refers to row; second integer to columns

#Change entry in matrix using indexing
matrix[0, 1] = a #note Python counts from 0

#Shape and size attributes
print(matrix.shape)
print(matrix.size)

#Pre-multiply the 3 by 4 matrix with a suitable all one row vector
ones = np.ones((1, matrix.shape[0]))

#Note that shape returns a list
#I can use indexing to access the number of rows

#Matrix multiplication
matrix_new = np.matmul(ones, matrix)

#Identity matrix
matrix_identity = np.eye(5)

#Descriptive statistics
print(matrix.sum())
print(matrix.mean())
print(matrix.std())

#Generating an axis or range for loops
idx = np.arange(1, 10, 0.1)
ldx = np.linspace(1, 10, 100)

#Horizontal and vertical stacks
#To combine data
matrix_a = np.array([[1, 2, 3], [3, 6, 8]])

matrix_b = np.array([[0, -2, 3], [4, -5, 1]])

print(matrix_a, matrix_b, sep = " and \n")

print("Horizontal")
print(np.hstack([matrix_a, matrix_b]))

print("Vertical")
print(np.vstack([matrix_a, matrix_b]))

#Changing dimensions
print(matrix_a.ravel())

print(matrix_a.flatten())

#Ravel and flatten look the same
#BUT careful: flatten returns a copy
rav = matrix_a.ravel()

flat = matrix_a.flatten()

#Changing rav and flat
flat[2] = 99
rav[2] = 99
