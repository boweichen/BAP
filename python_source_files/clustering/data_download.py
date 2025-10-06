"""
Data for cluster analysis
Source: https://algotrading101.com/learn/yfinance-guide/
"""

import yfinance as yf
import pandas as pd
import numpy as np

#Test our installation 
msft = yf.Ticker("MSFT")

#Income statement of Microsoft
df = msft.income_stmt
print(df.head())

print(type(df))

#All information on a ticker
print(msft.info)

#Dow Jones Industrial Average Stocks List
dj_list = [
	'MSFT',
	'AAPL',
	'AMZN',
	'V',
	'JPM',	
	'WMT',	
	'UNH',	
	'JNJ',	
	'PG',	
	'HD',	
	'MRK',	
	'CRM',	
	'CVX',	
	'KO',	
	'MCD',	
	'DIS',	
	'CSCO',	
	'INTC',	
	'IBM',	
	'VZ',	
	'CAT',	
	'AXP',	
	'AMGN',	
	'NKE',	
	'HON',	
	'GS',	
	'BA',	
	'MMM',	
	'TRV',	
	'DOW'	
	]

#Download data
#Start with empty DataFrame
dj_data = pd.DataFrame()

for ticker in dj_list:
	#Create Ticker() instance
	ticker_inst = yf.Ticker(ticker)
	#Convert from dictionary to DataFrame
	temp = pd.DataFrame.from_dict(ticker_inst.info)
	#Take most recent data (first row)
	#Add and update main data
	dj_data = pd.concat([dj_data, temp.iloc[[0]]])

#List of variables
var_list = [
	'symbol', 
	'marketCap', 
	'profitMargins',
	'priceToBook',
	'returnOnAssets',
	'returnOnEquity',
	'beta'
	]

#Replace marketCap in USD billions with log
dj_data['marketCap'] = np.log(dj_data['marketCap']/1000000000)

#Reassign DataFrame based on list of variables
dj_data = dj_data[var_list]

#Remove missing values
dj_data = dj_data.dropna()

#Remove index
dj_data.reset_index(drop = True, inplace = True)

print(dj_data)

#Descriptive statistics
print("\nDescriptive statistics:\n")

#Remove tickers
df = dj_data[var_list[1:]]
stats = df.describe()
print(stats)

#Export as LaTeX table
#This requires Jinja2
#Print to screen
output = stats.to_latex(
	formatters={"name": str.upper}, 
	float_format="{:.3f}".format,)

print(output)  

des_table = open('des_table.txt', 'w')
print(output, file = des_table)
des_table.close()

#Save DataFrame
dj_data.to_pickle("data_cluster.pkl")