"""
Pandas

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

#Import libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Change directory
# import os
# path = ""
# os.chdir(path)


#=========================================================================================================
#Import data
#=========================================================================================================
#Pandas DataFrame
data = pd.read_csv("hh_data.csv") 

# Preview the first 5 lines of the loaded data 
print(data.head())
print(data.tail())

#=========================================================================================================
#Scatter plot
#=========================================================================================================
data.plot.scatter(x = 'FIX_A', y = 'INC')
plt.savefig(r"DW_scatter.png")
plt.show()

#=========================================================================================================
#Pandas series
#=========================================================================================================
income = data['INC']
income = data.INC

#=========================================================================================================
#Indexing
#=========================================================================================================
income = data.iloc[:, 0]
income = data.iloc[:100, 0]

#=========================================================================================================
#Conditioning
#=========================================================================================================
income = data.INC[data.INC > 100000]
data = data[(data.INC > 100000) & (data.FIX_A > 100000)]

#=========================================================================================================
#NumPy array
#=========================================================================================================
income = data.INC.values

#=========================================================================================================
#Descriptive statistics
#=========================================================================================================
print("\nDescriptive statistics: Pandas Series\n") 
stats = data['INC'].describe() 
print(stats)

print("\nDescriptive statistics: Pandas DataFrame\n") 
stats = data.describe(include = 'all') 
print(stats)

#=========================================================================================================
#Histogram: distribution of variables
#=========================================================================================================
#Skewness
#Log transformation
# data['ln_INC'] = np.log(data['INC'])
data['ln_INC'] = data['INC'].transform(lambda x: np.log(x))

#Histograms
fig, axes = plt.subplots(nrows = 1, ncols = 2)
data['INC'].hist(ax = axes[0], color = 'red')
data['ln_INC'].hist(ax = axes[1], color = 'blue')
#Modifications
axes[0].set_title('Income')
axes[1].set_title('Log income')
plt.savefig('DW_transform.png')
plt.show()