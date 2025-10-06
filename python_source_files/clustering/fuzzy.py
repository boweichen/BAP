"""
Fuzzy C-means in Python
NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the pkl file.

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Load DataFrame
df = pd.read_pickle("data_cluster.pkl")
#print(df)

#Remove ticker symbols
df = df.iloc[:, 1:]

#Convert into NumPy array
data = df.values
#print(data)

#Dimension of data matrix
#Shape attribute returns a tuple 
#with number of rows and columnes
#print(data.shape)

#Number of clusters
clusters = 4

#Fuzziness parameter m
m = 2

#Initial cluster membership
#U refers to membership matrix
U = np.random.rand(data.shape[0], clusters)
#print(U)

#Probability that obs. is in one of the clusters
#Normalisation to ensure that row sum is one
row_sum = np.sum(U, axis=1)
#print(row_sum)

#Adds dimension as row_sum has shape (28,)
row_sum = row_sum[:, np.newaxis]

#Normalise U
U = np.divide(U, row_sum) 
#print(U)

#Cluster centre v_i (where i refers to cluster)
#\mu_{ij} is the membership degree of observation j
v1 = np.sum((U[:,0]**m)[:,np.newaxis]*data, axis = 0)/np.sum(U[:,0]**m)
#print(v1)

#This can be applied to all clusters
#Define shape of the cluster centre matrix
v = np.zeros((clusters, data.shape[1]))
for i in range(clusters):
    v[i,:]=np.sum((U[:,i]**m)[:,np.newaxis]*data, axis = 0)/np.sum(U[:,i]**m)
#print(v)

#Define function
def cluster_centre(clusters, data, U):
	v = np.zeros((clusters, data.shape[1]))
	for i in range(clusters):
	    v[i,:]=np.sum((U[:,i]**m)[:,np.newaxis]*data, axis = 0)/np.sum(U[:,i]**m)
	return v

#Call function
v = cluster_centre(clusters, data, U)
#print(v)

#Membership degree \mu_{ij}
#Objective function: loss function - aim is to minimise the function
#Order = 2 is the default - Euclidean distance
def membership_degree(clusters, data, v, m):
	#Dimension of membership degree array
    U = np.zeros((data.shape[0], clusters))
    #Euclidean distance
    d = np.zeros((data.shape[0], clusters))
    for i in range(clusters):
        d[:, i] = np.linalg.norm(data - v[i,:], ord  = 2, axis = 1)

    U = 1 / (d**(2/(m-1))*np.sum((1/d)**(2/(m-1)), axis = 1 )[:, np.newaxis])
    return U

print(f"First observation is initially in cluster {np.argmax(U, axis = 1)[0]}.")
print(f"It has membership degree of {U[np.argmax(U, axis = 1)[0], 0]}.")

#Updated membership degree
U = membership_degree(clusters, data, v, m)
print(f"\nAfter updating, the first observation is in cluster {np.argmax(U, axis = 1)[0]}.")
print(f"With membership degree of {U[np.argmax(U, axis = 1)[0], 0]}.")

#Iterations L
L = 10
for _ in range(L):
    v = cluster_centre(clusters, data, U)
    U_updated = membership_degree(clusters, data, v, m)
    print(U_updated[0, :])
    print(np.argmax(U_updated, axis = 1)[0])
    U = U_updated

