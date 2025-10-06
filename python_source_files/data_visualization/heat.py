"""
Heatmap

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#Import data as DataFrame
df = pd.read_csv("uk_reserves.csv")

#Check the data structure
print(df.head())
print(df.tail())

#Drop Year
df = df.drop(columns = ['year'])

#Correlation matrix
corr_matrix = df.corr()

#Heat map
sns.heatmap(corr_matrix)
plt.savefig('DV_heat.png')
plt.show()