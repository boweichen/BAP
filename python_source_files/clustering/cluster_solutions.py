"""
Cluster solutions
"""

import numpy as np
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
from sklearn.cluster import KMeans

#Load Iris dataset
X, y = datasets.load_iris(return_X_y = True)

iris = datasets.load_iris()
X = iris.data
y = iris.target

#Check the data structure
print(X)
print(f"\nThese are the true labels {y}.")

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

#Fuzzy c_means with four or five clusters
c_means = CMeans(clusters = 4, m = 2, data = X)

c_means.initialisation()
print(c_means.U)

c_means.cluster_centre()
print(c_means.v)

c_means.membership_degree()
print(c_means.U)

c_means.fit()

#Labels
labels_4 = np.argmax(c_means.U, axis = 1)
print(labels_4)

#Increase to 5 clusters
c_means_5 = CMeans(clusters = 5, m = 2, data = X)
c_means_5.initialisation()
c_means_5.fit()

#Labels
labels_5 = np.argmax(c_means_5.U, axis = 1)
print(labels_5)

#The Silhouette Coefficient
silhouette_4 = metrics.silhouette_score(X, labels_4, metric='euclidean')
silhouette_5 = metrics.silhouette_score(X, labels_5, metric='euclidean')
print(f"The Silhouette Coefficient is {round(silhouette_4, 3)} with 4 clusters and {round(silhouette_5, 3)} with 5 clusters.")


