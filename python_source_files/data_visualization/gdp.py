"""
GDP per capita data

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

#Import data as DataFrame
df = pd.read_csv("gdp.csv")

#Set index
df = df.set_index(df['Year'])

#Change float to integer for Year
df = df.astype(int)

#Inspect the data
print(df.head())
print(df.tail())

#Multiple lines
sns.lineplot(data = df[['ARG', 'AUS', 'AUT', 'BRA', 'GBR']])

plt.savefig('DV_gdp.png')
plt.show()

#Log transformation
df[['ARG', 'AUS', 'AUT', 'BRA', 'GBR']] = np.log(df[['ARG', 'AUS', 'AUT', 'BRA', 'GBR']])

#Standard deviation of log GDP per capita in each year
df['DIV'] = df[['ARG', 'AUS', 'AUT', 'BRA', 'GBR']].std(axis = 1)

#Plot measure of convergence
sns.lineplot(data = df['DIV'])
plt.savefig('DV_convergence.png')
plt.show()