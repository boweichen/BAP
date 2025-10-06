"""
Illustration of linear regression
"""

import matplotlib.pyplot as plt
import numpy as np

#Independent variable x axis
x = np.array([1,5,3,7,2,11])
#Dependent variable y axis
y = np.array([2,4,1,5,3,7])
#Scatter plot
plt.scatter(x, y)
#Naming axes
plt.xlabel('x - axis')
plt.ylabel('y - axis')

#Straight line
y_hat = 0.7*x
plt.plot(x, y_hat, color='green')

#Example deviation
x1 = np.array([2, 2])
y1 = np.array([2.9, 1.5])
plt.plot(x1, y1, color='red')

#Save figure
plt.savefig("reg_illustration.png") 
plt.show()