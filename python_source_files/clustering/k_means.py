"""
K-means in Python

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the pkl file.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

#Load DataFrame
df = pd.read_pickle("data_cluster.pkl")
print(df)

#We use tickers as labels - no information
y = df['symbol']
X = df.iloc[:, 1:]

#Correlation matrix
print(X.corr())

#Select ROA, PTB, and Beta
#Convert to NumPy array
X = df[['priceToBook', 'returnOnAssets', 'beta']].values

#Select the number of clusters
estimators = [
    ("k_means_5", KMeans(n_clusters = 5)),
    ("k_means_4", KMeans(n_clusters = 4)),
    ("k_means_3", KMeans(n_clusters = 3)),
    ("k_means_2", KMeans(n_clusters = 2))
]

fig = plt.figure(figsize=(10, 8))
titles = ["Five clusters", "Four clusters", "Three clusters", "Two clusters"]
for idx, ((name, est), title) in enumerate(zip(estimators, titles)):
    ax = fig.add_subplot(2, 2, idx + 1, projection="3d", elev = 45, azim = 50)
    est.fit(X)
    labels = est.labels_

    scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(float), edgecolor = 'k')
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.zaxis.set_ticklabels([])
    ax.set_xlabel("PTB")
    ax.set_ylabel("ROA")
    ax.set_zlabel("Beta")
    ax.set_title(title)

plt.subplots_adjust(wspace = 0.05, hspace = 0.15)
plt.savefig("Cluster_K_means.png") 
plt.show()


from sklearn.metrics import silhouette_score
kmeans = KMeans(n_clusters=2, random_state=42)
print(silhouette_score(X, kmeans.fit_predict(X)))