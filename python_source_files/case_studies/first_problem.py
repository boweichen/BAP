"""
Optimal routes
"""
import pulp as pp

#Default is a minimisation 
#Set sense = -1 for maximising profit
model = pp.LpProblem("Optimal production", sense = -1)

#Model parameters
#Capacity constraints of factories
capacity = [
    1000,
    700
    ]

#Variable costs
var = [
    10,
    7]

#Price
price = 11

#Demand
demand = 1500

#Define decision variables
#Lower and upper bounds
#Types
fac1 = pp.LpVariable('Factory 1', lowBound = 0, upBound = capacity[0], cat = "Continuous")
fac2 = pp.LpVariable('Factory 2', lowBound = 0, upBound = capacity[1], cat = "Continuous")

#Define objective function
model += price * (fac1 + fac2) - var[0] * fac1 - var[1] * fac2

#Define constraint based on total demand
model += fac1 + fac2 <= demand 
       
#Solve model
model.solve()
print(f"{fac1.varValue} in Factory 1 and {fac2.varValue} in Factory 2.")