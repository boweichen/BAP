"""
Validity of cluster analysis
"""
import numpy as np
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
from sklearn.cluster import KMeans

#Load Iris dataset
X, y = datasets.load_iris(return_X_y = True)

#Three labels, which are known
print(y)

#Data matrix with four dimensions
#150 observations
print(X.shape)

#K-means cluster analysis
kmeans_model = KMeans(n_clusters = 3).fit(X)
predict_y = kmeans_model.labels_
print(predict_y)

#Rand index
rand_index = metrics.rand_score(y, predict_y)
rand_index_adj = metrics.adjusted_rand_score(y, predict_y)
print(f"The Rand index is {rand_index}, and the adjusted score is {rand_index_adj}.")

#K-means cluster analysis with 4 clusters
kmeans_model_4 = KMeans(n_clusters = 4).fit(X)
predict_4_y = kmeans_model_4.labels_

#The Silhouette Coefficient
silhouette_3 = metrics.silhouette_score(X, predict_y, metric='euclidean')
silhouette_4 = metrics.silhouette_score(X, predict_4_y, metric='euclidean')
print(f"The Silhouette Coefficient is {round(silhouette_3, 3)} with 3 clusters and {round(silhouette_4, 3)} with 4 clusters.")