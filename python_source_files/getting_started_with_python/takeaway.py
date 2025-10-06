"""
Takeaway: First coding challenge
"""
#Create a list of food items
food_list = [
        'pizza',
        'pasta',
        'burger'
        ]

#Create a list of prices
price_list = [
    10,
    7.5,
    5]

#The input function
print('Welcome to Cheap Cuts')
name = input('Enter your name: ')

#==========================================================#
#First attempt
#==========================================================#
#Make an order
order_list = []

for food in food_list:
    order = input(f'{name} do you want {food}?: [y/n] ')
    if order == 'y':
        order_list.append(1)
    elif order == 'n':
        order_list.append(0)
    else:
        print(f'Sorry {name} I do not understand you')


#==========================================================#
#Second attempt
#==========================================================#
#Make an order
order_list = []

for food in food_list:
    order_incomplete = True
    while order_incomplete:
        order = input(f'{name} do you want {food}?: [y/n] ')
        if order == 'y':
            order_list.append(1)
            order_incomplete = False
        elif order == 'n':
            order_list.append(0)
            order_incomplete = False
        else:
            print(f'Sorry {name} I do not understand you')

#==========================================================#
#Third attempt
#==========================================================#
#Make an order
order_list = []

for food in food_list:
    order_incomplete = True
    while order_incomplete:
        order = input(f'{name} do you want {food}?: [y/n] ')
        if order == 'y':
            num = input(f'How many {food}s do you want? ')
            order_list.append(int(num))
            order_incomplete = False
        elif order == 'n':
            order_list.append(0)
            order_incomplete = False
        else:
            print(f'Sorry {name} I do not understand you')
            
print(f'\nThanks {name} for ordering {order_list[0]} {food_list[0]}s')
print(f'{order_list[1]} {food_list[1]}s and {order_list[2]} {food_list[2]}s')

total_price = sum([order * price for order, price in zip(order_list, price_list)])

print(f'Please pay GBP {total_price}')