"""
Scatter plots

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""
import pandas as pd
import plotly.express as px

#Import data as DataFrame
df = pd.read_csv("policy_ranking.csv")

#Remove missing values
df = df.dropna()

#Change column name
df = df.rename(columns = {"Country Name": "Country", "Time": "Year", "Value": "CPIA"})

#Change float to integer for Year
df['Year'] = df['Year'].astype(int)

#Check the data structure
print(df.head())
print(df.tail())

#Define a list of years
years_selected = [2005, 2010, 2015, 2022]

#Select years
df = df[df['Year'].isin(years_selected)]

#Scatter
fig = px.scatter(df, x = "Year", y = "CPIA")
fig.show()