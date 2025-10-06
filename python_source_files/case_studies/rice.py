"""
Rice prices and stock
NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.
"""

import pandas as pd
import matplotlib.pyplot as plt

#Import csv files as DataFrame
file = "rice_data.csv"
df = pd.read_csv(file)
print(df.head())

#Remove redundant columns
df = df[['Time', 'price', 'stock']]
print(df.head())

#Plot time series
#Set index
df = df.set_index('Time')
fig1, axes = plt.subplots(nrows=2, ncols=1)
axes[0].set_title('Price of rice')
axes[1].set_title('Stock of rice')
df.price.plot(ax = axes[0], color = 'blue')
df.stock.plot(ax = axes[1], color = 'red')
plt.tight_layout()
fig1.savefig("CS_price.png") 
plt.show()