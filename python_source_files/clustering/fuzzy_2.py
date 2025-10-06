"""
Fuzzy C-means in Python
Version 2

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


class CMeans():
    def __init__(self, data, clusters = 2, m = 2, L = 100, stop = 0.001):
        """
        clusters: Number of clusters
        m: Fuzziness parameter
        L: Iterations
        stop: Stopping criterion
        data: Data as a Numpy array
        U: Cluster membership matrix
        v: Cluster centres
        """
        self.data = data
        self.clusters = clusters
        self.m = m
        self.L = L
        self.stop = stop
        self.U = np.empty((self.data.shape[0], self.clusters))
        self.v = np.empty((self.clusters,self.data.shape[1]))
        self.reached = False

    def initialisation(self):
        """
        Initial cluster membership matrix: random and normalised
        """
        U = np.random.rand(self.data.shape[0], self.clusters)
        row_sum = np.sum(U, axis=1)[:, np.newaxis]
        U = np.divide(U, row_sum) 
        self.U = U

    def cluster_centre(self):
        """
        Determines centre of cluster based on current cluster membership matrix
        """
        for i in range(self.clusters):
            self.v[i,:]=np.sum((self.U[:,i]**self.m)[:,np.newaxis]
            *self.data, axis = 0)/np.sum(self.U[:,i]**self.m)

    def membership_degree(self):
        """
        Updates cluster membership matrix
        """
        #Update cluster centres
        self.cluster_centre()
        #Euclidean distance
        d = np.zeros((self.data.shape[0], self.clusters))
        for i in range(self.clusters):
            d[:, i] = np.linalg.norm(self.data - self.v[i,:], ord  = 2, axis = 1)

        self.U = 1 / (d**(2/(self.m-1))*np.sum((1/d)**(2/(self.m-1)), axis = 1 )[:, np.newaxis])

    def stopping_criterion(self):
        """
        Stopping criterion based on max adjustment
        """
        #Euclidean distance
        d = np.zeros(self.U.shape)
        #Update cluster membership matrix
        U_old = self.U[:]
        self.membership_degree()
        d = max(np.linalg.norm(self.U-U_old, ord = 2, axis = 1))
        if d <= self.stop:
            self.U = U_old
            self.reached = True
            print("stop")

    def fit(self):
        """
        Update until stopping criterion or max iteration
        """
        #Iteration left
        l = self.L

        while l and not self.reached:
            print(l)
            l -= 1
            self.stopping_criterion()

c_means = CMeans(clusters = 4, m = 2, data = data)

c_means.initialisation()
print(c_means.U)

c_means.cluster_centre()
print(c_means.v)

print(f"First observation is initially in cluster {np.argmax(c_means.U, axis = 1)[0]}.")
print(f"It has membership degree of {c_means.U[np.argmax(c_means.U, axis = 1)[0], 0]}.")

#Updated membership degree
c_means.membership_degree()
print(f"\nAfter updating, the first observation is in cluster {np.argmax(c_means.U, axis = 1)[0]}.")
print(f"With membership degree of {c_means.U[np.argmax(c_means.U, axis = 1)[0], 0]}.")

c_means.stopping_criterion()

c_means.fit()

