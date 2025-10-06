"""
Linear Regression

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col
from sklearn.linear_model import LinearRegression
#from statsmodels.graphics.regressionplots import abline_plot

#STEP 1: Data import
#Import csv files as DataFrame
file = "UK_property_data.csv"
df = pd.read_csv(file)
print(df.head())

#STEP 2: Convert date variable
#Note time_split is a Pandas Series
df['time_split'] = df.time.str.split("-")
print(df.time_split)

#Create year and month variable
df['year'] = df.time_split.apply(lambda x: int(x[0]))
df['month'] = df.time_split.apply(lambda x: int(x[1]))

#Remove unwanted columns
df = df.drop('time_split', axis=1)

#Check DataFrame
print(df.head())

#STEP 3: Plot time series
#Set index
df = df.set_index('time')
fig1, axes = plt.subplots(nrows=2, ncols=1)
axes[0].set_ylabel('Price')
axes[1].set_ylabel('Volume')
df.price.plot(ax=axes[0])
df.volume.plot(ax=axes[1], color='red')
plt.tight_layout()
fig1.savefig("reg_series.png") 
plt.show()


#STEP 4: Seasonal adjustment and lags
df['adj_price'] = (df.price-df.price.shift(12)).shift(1)
df['adj_volume'] = df.volume-df.volume.shift(12)
df['d_volume'] = df.volume.diff()
fig2, axes = plt.subplots(nrows=2, ncols=1)
axes[0].set_ylabel('Volume')
axes[1].set_ylabel('Adjusted')
df.d_volume.plot(ax=axes[0], color='green')
df.adj_volume.plot(ax=axes[1], color='red')
plt.tight_layout()
fig2.savefig("reg_adjustment.png") 
plt.show()


#STEP 5: Regression models
mod1 = smf.ols('adj_volume ~ adj_price', data=df)
res1 = mod1.fit()
print(res1.summary())

#STEP 6: Create year dummies
year_dummies = pd.get_dummies(data = df.year, prefix = 'Y')
df = df.join(year_dummies)
print(df.head())


#STEP 7: Second model with year effects, 2005-2023
mod2 = smf.ols('adj_volume ~ adj_price + Y_2008 + Y_2009', data=df)
res2 = mod2.fit()
print(res2.summary())


#STEP 8: Regression tables
info_dict={'N':lambda x: "{0:d}".format(int(x.nobs)),'R2':lambda x: "{:.2f}".format(x.rsquared)}
dfoutput = summary_col([res1,res2],stars=True,float_format="%0.3f", \
model_names=['Reference', 'Year'], info_dict=info_dict, \
regressor_order=['const','adj_price','Y_2008','Y_2009'])
print(dfoutput)
dfoutput.as_latex() 
with open('reg_table1.tex','w') as tf: 
    tf.write(dfoutput.as_latex()) 


#STEP 9: Alternative approach
#Remove missing values
df = df.dropna()
#Define data matrix from DataFrame
#Convert to NumPy array
X = df[['adj_price', 'Y_2008','Y_2009']].values
#Select dependent variable
y = df['adj_volume'].values
reg = LinearRegression().fit(X, y)
#Show coefficients
print(reg.coef_)


#STEP 10: Model predictions
#Re-estimate our model using NumPy
#Many alternatives, e.g., abline_plot
#NumPy function obtains alpha (intercept) and beta (slope) of linear regression
beta, alpha = np.polyfit(df['adj_price'], df['adj_volume'], 1)
#Scatter plot
plt.plot(df['adj_price'], df['adj_volume'], 'o', color = 'gray', markersize = 2)
#Add regression line
plt.plot(df['adj_price'], alpha+beta*df['adj_price'], color = 'orange')
plt.savefig("reg_predict.png") 
plt.show()


#============================= OUTTAKES ==========================================================
#Alternative models
# mod2 = smf.ols('adj_volume ~ adj_price + Y_2008 + Y_2009', data=df)
# res2 = mod2.fit()

# #Confidence interval
# summary = res2.get_prediction(df).summary_frame()
# #Ignores index
# summary['adj_price'] = df['adj_price'].values
# summary['adj_volume'] = df['volume'].values
# summary['fitted values'] = res2.fittedvalues.values
# #summary = summary.sort_values('adj_price')


# fig3, ax = plt.subplots()

# # print(summary)
# # print(df['adj_price'])

# ax = summary.plot.scatter(x = 'adj_price', y = 'fitted values', color = 'blue')

# #Predicted and actual values
# ax = summary.plot.scatter(x = 'adj_price', y = 'adj_volume', color = 'red')


# # adding title to the plot 
# plt.title('Open Price Plot') 
  
# # adding Label to the x-axis 
# plt.xlabel('Years') 
  
# # adding legend to the curve 
# plt.legend() 

# #print(res2.fittedvalues)

# #Plot regression line
# #abline_plot(model_results = res2, ax = ax, color = 'orange')

# #Plot confidence interval
# #ax.fill_between(x = summary['adj_price'], y1 = summary['mean_ci_lower'], y2 = summary['mean_ci_upper'],
#                 #alpha = 0.2, color = 'orange')

# #summary['fitted values'].plot()

# plt.show()


# mod = smf.ols('adj_volume ~ adj_price + Y_2008 + Y_2009', data=df).fit()
# fig = abline_plot(model_results=mod)
# ax = fig.axes[0]
# ax.scatter(X[:,1], y)
# ax.margins(.1)
# plt.show()