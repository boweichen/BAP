"""
Climate risk

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

"""Get some data"""
#Change directory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#Import data
df = pd.read_csv("vul_data.csv") 

#Drop missing values
df = df.dropna(how='any')

#Countries in top 10% based on VUL measure
high = df.VUL.quantile(.9)

#Take values for index
vul = df.iloc[:, 2].values

#Dummy for high-risk country
y = np.where(vul >= high, 1, -1)

#Define data matrix
X = df.iloc[:, 4:].values

# We split the sample into 70% training and 30% test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
                     stratify=y,
                     random_state=0)

#Standardisation
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)


#Covariance matrix
cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eigh(cov_mat)
print('\nEigenvalues \n%s' % eigen_vals)

#Sort eigenvalues
tot = sum(eigen_vals)
var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)]
cum_var_exp = np.cumsum(var_exp)

#Plot eigenvalues
plt.bar(range(1, 27), var_exp, alpha=0.5, align='center',
        label='individual explained variance')
plt.step(range(1, 27), cum_var_exp, where='mid',
         label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal component index')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('PCA_Task_Fig1.png', dpi=300)
plt.show()

#List of (eigenvalue, eigenvector) tuples
eigen_pairs = [(np.abs(eigen_vals[i]), eigen_vecs[:, i])
               for i in range(len(eigen_vals))]

#Sort the (eigenvalue, eigenvector) tuples from high to low
eigen_pairs.sort(key=lambda k: k[0], reverse=True)
w = np.hstack((eigen_pairs[0][1][:, np.newaxis],
               eigen_pairs[1][1][:, np.newaxis]))
print('Matrix W:\n', w)

X_train_std[0].dot(w)
X_train_pca = X_train_std.dot(w)
colors = ['r', 'b']
markers = ['o', 'x']

for l, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(X_train_pca[y_train == l, 0], 
                X_train_pca[y_train == l, 1], 
                c=c, label=l, marker=m)

plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.savefig('PCA_Task_Fig2.png', dpi=300)
plt.show()



