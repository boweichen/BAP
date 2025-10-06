"""
CO2 emission analysis
NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

import pandas as pd
import matplotlib.pyplot as plt

#Import data as DataFrame
df = pd.read_csv("co2_emissions.csv")

print(df.head())

#Set index
df = df.set_index(df['Year'])

print(df.head())

#Aggregated data over time
df['Emission'][df['Entity'] == 'World'].plot(title = 'Global Emissions', ylabel = 'CO2 Emission', logy = True)

#Save figure
plt.savefig('DV_world.png')
plt.show()

#Top 5 countries by emission 2022
#Drop missing values
#Ignore aggregated indices
df_top = df[(df['Code'] != 'OWID_WRL') & (df['Year'] == 2022)].dropna()

#Sort by CO2 emissions in 2022
#Select top 5
df_top = df_top.sort_values(by = ['Emission'], ascending = False).iloc[:5,:]
print(df)

#Add selected countries to a list
countries = df_top['Entity'].tolist()
print(countries)

#Go back to the original dataset
#Select the top 5 countries

#Plot top 5 countries over time
#Ignore aggregated indices
df = df[(df['Code'] != 'OWID_WRL') & (df['Year']>=1900)].dropna()
df = df[df['Entity'].isin(countries)]
print(df)

grouped = df.groupby('Code')
for key, group in grouped:
	plt.plot(group.Year, group.Emission, label = key)
plt.legend()
plt.savefig('DV_top_5.png')
plt.show()

#Cumulated emissions
grouped = df.groupby('Code')
print(grouped)
for key, group in grouped:
	plt.plot(group.Year, group.Emission.cumsum(), label = key)
plt.legend()
plt.savefig('DV_top_5_cum.png')
plt.show()