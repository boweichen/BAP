"""
Health expenditure

NOTE: You might need to use os.chdir() or rename the dataset
depending on where you stored the CSV file.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col

#Import csv files as DataFrame
file = "health.csv"
df = pd.read_csv(file)
print(df.head())

#Remove missing values
df = df.dropna()
print(df.head())

#Regression model
model = smf.ols('h_exp ~ DHI + pop + r_gdp', data = df)
res = model.fit()
print(res.summary())