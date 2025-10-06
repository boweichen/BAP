"""
Outsourcing
"""

import pulp as pp

#Location of factories
factories = ["UK", "India"]

#Five markets
markets = ["UK", "France", "China", "Japan", "India"]

#Demand in each market
demand = {
    "UK": 100,
    "France": 150,
    "China": 200,
    "Japan": 90,
    "India": 80,
}

#Matrix (array) of delivery costs
delivery = [  
    [1, 2, 5, 4, 3],  
    [3, 3, 2, 2, 1],  
]

#Use keys in new dictionary capturing delivery costs
#Rows refer to factories
#Columns refer to markets
costs = pp.makeDict([factories, markets], delivery, 0)

#Check the array
print(costs)

#Create instance of the cost minimisation problem
#Minimisation by default
model = pp.LpProblem("Outsourcing")

#List comprehension
#List of tuples for all factory-market pairs
routes = [(factory, market) for factory in factories for market in markets]

#Check routes
print(routes)

#Dictionary containing routes
var_routes = pp.LpVariable.dicts('routes', (factories, markets), lowBound = 0, upBound = None, cat = "Integer")
print(var_routes)

#Objective function added
model += (
    pp.lpSum([var_routes[factory][market]*costs[factory][market] for (factory, market) in routes]),
    "Sum of delivery costs with outsourcing",
)

#Minimum demand constraints
for market in markets:
    model += (
        pp.lpSum([var_routes[factory][market] for factory in factories]) >= demand[market],
        f"Total goods delivered to {market}",
    )

#Solve model
model.solve()

print("Status:", pp.LpStatus[model.status])

#Show variables
for var in model.variables():
    print(var.name, "=", var.varValue)

#Optimised delivery costs with outsourcing
costs_out = model.objective.value()
print(f"Total costs using outsourcing = {costs_out}")

#Comparison: UK production without outsourcing

costs_uk = 0

for market in markets:
	costs_uk += demand[market]*costs["UK"][market]

print(f"Total costs without outsourcing = {costs_uk}")
print(f"\nYou can invest up to {round(costs_uk - costs_out, 0)} in India to outsource production.")