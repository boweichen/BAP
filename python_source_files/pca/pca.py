"""
PCA

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the dta file.

"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Additional import statements for the alternative implementation
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


#Data import from dta file (Stata data format)
df = pd.read_stata('data_import.dta')  
print(df.head())

#Define the data matrix, which refers to a NumPy array
X = df.values

#Split data into training and test data
X_train, X_test = train_test_split(X, test_size=0.3, random_state=0)

#Standardisation
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

#Covariance, eigenvalues, and eigenvectors
cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eigh(cov_mat)
print('\nEigenvalues \n%s' % eigen_vals)

#Sorting eigenvalues
tot = sum(eigen_vals)
var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

#Derive the transformation matrix W
eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i])
               for i in range(len(eigen_vals))]

eigen_pairs.sort(key=lambda k: k[0], reverse=True)
w = np.hstack((eigen_pairs[0][1][:, np.newaxis],
               eigen_pairs[1][1][:, np.newaxis]))
print('Matrix W:\n', w)

#Transforming the original dataset
X_train_pca = X_train_std.dot(w)
X_test_pca = X_test_std.dot(w)

#Alternative implementation
pca = PCA()
X_train_pca = pca.fit_transform(X_train_std)
exp_var = pca.explained_variance_ratio_

#Focusing on two principal components
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca = pca.transform(X_test_std)
plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1])
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.savefig("PCA_transformed.png") 
plt.show()

#Visualisation and interpretation of PCA
#Max number of principal components
max_num = 15

#Construct x axis
x = np.arange(max_num)

plt.bar(x, var_exp[:max_num], alpha=0.5, align='center',
        label='Explained variance')
plt.step(x, cum_var_exp[:max_num], where='mid',
         label='Cumulative explained variance')
plt.ylabel('Explained variance')
plt.xlabel('Principal component')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('PCA_variance.png', dpi=300)
plt.show()

#Scree plot
plt.plot(eigen_vals[::-1])
plt.ylabel('Eigenvalue')
plt.xlabel('Component number')
plt.savefig('PCA_screeplot.png', dpi=300)
plt.show()
