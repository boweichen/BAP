"""
Cournot game with heterogeneous agents
"""

import numpy as np
import matplotlib.pyplot as plt

"""Setup"""
N = 100 #Number of firms
costs = [] #Array of marginal costs; empty list

"""Random seed"""
np.random.seed(7) #Initialize random number generator

"""Set default parameters"""
alpha = 20
beta = 0.1
rho = 0.1 #Discount rate


"""Distribution of marginal costs"""
mu_c = 1
sigma_c = 1

for _ in range(N):
    costs.append(abs(np.random.normal(mu_c, sigma_c)))
 
    
""""Average quantity"""    
def average_quantity(costs: list, alpha: int, beta: int, N: int):
    return (alpha - np.mean(costs))/(beta * (N + 1))


"""Market price""" 
def market_price(costs: list, alpha: int, N: int):
    return alpha - N/(N + 1) * (alpha - np.mean(costs))

"""Optimal output"""
"""
Returns the outputs which can be negative in the case of high cost firms
"""
def optimal_output(costs: list, alpha: int, beta: int, N: int):
    output = []
    av_quant = average_quantity(costs, alpha, beta, N)
    for cost in costs:
        output.append((alpha - cost)/beta - N * av_quant)         
    return output

"""Call function"""
out = optimal_output(costs, alpha, beta, N)

"""Remove firm with most negative output recursively"""
while min(out) < 0:
    del costs[out.index(min(out))] #Remove costs that belong to firm with smallest output
    N -= 1 #Reduce the number of firms by one
    out = optimal_output(costs, alpha, beta, N)  
    
    
"""Market price"""
price = market_price(costs, alpha, N)


"""Period revenue"""
def firm_revenue(price: int, costs: list, out: list):
    rev = []
    for idx in range(len(out)):
        rev.append((price - costs[idx]) * out[idx])
    return rev

revenue = firm_revenue(price, costs, out)


"""Firm value"""
def firm_value(revenue: list, rho: int):
    return [rev/rho for rev in revenue if rev > 0]
        
value = firm_value(revenue, rho)


"""Distribution of firm value""" 
data = value

bins = np.arange(0, max(data), 1.5) # fixed bin size

plt.xlim([min(data), max(data)])

plt.hist(data, bins=bins, alpha=0.5)
plt.title('Distribution of firm value')
plt.xlabel('Firm value')
plt.ylabel('Count')

plt.show()


"""Accumulation of cash"""
def cash(revenue: list, time: int = 1):
    return [ rev * time for rev in revenue ]

time = 1
cash_stock = cash(revenue, time)

"""Cash mergers"""
"""
The best_target function identifies the best target for bidder.
This target maximises the bidder's increase in value.
It returns in index position of the best target
"""

def best_target(costs: list, revenue: list, value: list, cash_stock: list, N: int, alpha: int, beta: int):
    benefit_for_bidder = []
    for __ in range(N):
        #Copies of lists
        N_copy = N
        costs_copy = costs[:]
        revenue_copy = revenue[:]
        value_copy = value[:]
        cash_copy = cash_stock[:]
        
        #Checks conditons for any firm in list
        cash_merger = max(cash_copy) > value_copy[__] #Boolean whether cash merger is possible
        pre_merger_value = value[revenue_copy.index(max(cash_copy))] #Bidder
        target_value = value_copy[__] #Values of i's firm
        
        if cash_merger:
            del costs_copy[value_copy.index(value_copy[__])] #Remove costs that belong to target firm i
            N_copy -= 1 #Reduce the number of firms by one
        
            #Outputs, price, and value after merger     
            out_new = optimal_output(costs_copy, alpha, beta, N_copy)    
            price_new = market_price(costs_copy, alpha, N_copy)
            revenue_new = firm_revenue(price_new, costs_copy, out_new)
            value_new = firm_value(revenue_new, rho)
        
            post_merger_value = max(value_new)
            benefit_for_bidder.append(post_merger_value - pre_merger_value - target_value)
        else:
            benefit_for_bidder.append(0)
    return benefit_for_bidder.index(max(benefit_for_bidder))

index_bidder = cash_stock.index(max(cash_stock))
index_target = best_target(costs, revenue, value, cash_stock, N, alpha, beta)
index_cheapest = value.index(min(value))





"""The cheapest target is not the best target"""
print(f"Is the statement that the highest valued firm will\n \
      acquire the lowest valued firm correct?\n Answer: {index_target == index_cheapest}")