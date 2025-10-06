"""
Functions
"""

#==================================================================================
#Functions
#==================================================================================
#Take any integer to the power of another integer
x = 5
a = 3

result = x**a
print(f'{x} to the power of {a} is {result}.')

#==================================================================================
#First function
#==================================================================================
#Defining our own functions
#Keyword def

def power(x, a):
    out = x**a
    print(f'{x} to the power of {a} is {out}.')

#Invoke a function or call a function
#Keywords or positional arguments
#Scope of variable out
power(x = 5, a = 3)

#==================================================================================
#Return
#==================================================================================
#Return 
def power(x, a):
    out = x**a
    print(f'{x} to the power of {a} is {out}.')
    return out

out = power(5, 3)

#==================================================================================
#Coding challenge
#==================================================================================
"""
Write a function that asks for user input. Users should input integers, and
the function returns the sum and product of all integers entered.
The process stops when the user enters 0.
"""

def input_num():
    invalid_input = True
    
    while invalid_input:
        num = input("Please enter an integer. Enter 0 to stop: ")
        try: 
            num = int(num)
            invalid_input = False
        except:
            print('Invalid input')
    return num

def sum_product():
    #Sum and product of numbers entered        
    sum_num = 0
    prod_num = 1
    
    #Call first number
    num = input_num()
        
    while num:
        sum_num += num
        prod_num *= num
        num = input_num()
        
    print(f"The sum of integers is {sum_num}")
    print(f"The product of integers is {prod_num}")
    
#Call function
sum_product()