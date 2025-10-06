"""
Saving and loading data 
"""

import tkinter as tk
import pickle

from user import User

#Starts root
root = tk.Tk()
root.title('Portfolio Management')

#Size
root.geometry("500x600")

#Frames
frm = tk.Frame(root)
frm.grid(column = 0, row = 0)

"""
Functions for buttons
"""
def do_nothing():
	print("Do nothing!")


def start_button_function():
    """Function for start button"""
    #Get first and last name from entry widget
    f_name_get = f_name.get()
    l_name_get = l_name.get()

    #Get gender
    gender_get = gender.get()

    #Close new_game_window
    new_user_window.destroy()

    #Create global variables
    global user

    #Initialize user
    user = User(f_name = f_name_get, l_name = l_name_get, gender = gender_get)

    #CHECK
    print(f"{user.f_name} {user.l_name} entered {user.gender}.")


def new_user():
    #New window
    global new_user_window
    new_user_window = tk.Toplevel()
    new_user_window.title('New User')
    
    #Size of widget
    new_user_window.geometry("400x300")
    
    #Create global variables
    global f_name
    global l_name
    global gender

    f_name = tk.StringVar() 
    l_name = tk.StringVar() 

    #Entry: first and last name
    f_name_entry = tk.Entry(new_user_window, width = 30, textvariable = f_name)
    f_name_entry.grid(row = 0, column = 1, padx = 20)  
     
    l_name_entry = tk.Entry(new_user_window, width = 30, textvariable = l_name)
    l_name_entry.grid(row = 1, column = 1, padx = 20) 

    #Labels for entry
    f_name_label = tk.Label(new_user_window, text = "First name")
    f_name_label.grid(row = 0, column = 0)
    
    l_name_label = tk.Label(new_user_window, text = "Last name")
    l_name_label.grid(row = 1, column = 0)   

    #Radio button
    gender = tk.IntVar()
    gender.set('1')

    #Options for radio button as list of tuples
    OPTIONS = [('Male', '0'), ('Female', '1')]

    for option in OPTIONS:
        radio_button = tk.Radiobutton(new_user_window, text = option[0], variable = gender, \
        value = option[1])
        radio_button.grid(row = int(option[1]) + 2, column = 1)

    #Create start button
    start_button = tk.Button(new_user_window, text = "Start", command = start_button_function)
    start_button.grid(row = 4, column = 1, columnspan = 2, \
    ipadx = 115, padx = 10, pady = 1)


def save():
    """Saves objects; overwrites any existing file; default file 'portfolio.pkl'"""
    obj = [user]
    with open('portfolio.pkl', 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    #CHECK
    print(f"{user.f_name} SAVED.")


def load():
    """Loads objects"""
    with open('portfolio.pkl', 'rb') as input:
        obj = pickle.load(input)
    global user
    user = obj[0]

    #CHECK
    print(f"{user.f_name} LOADED.")

"""
Menu bar   
"""
menubar = tk.Menu(root)

#File menu
file_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label = "New", command = new_user)
file_menu.add_command(label = "Save", command = save)
file_menu.add_command(label = "Load", command = load)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.destroy)
menubar.add_cascade(label = "File", menu = file_menu)

#Invest menu
invest_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Invest", menu = invest_menu)

#Adds submenu to Buying: 
buy_sub_menu = tk.Menu(menubar, tearoff = 0)
buy_sub_menu.add_command(label = "Stocks", command = do_nothing)
buy_sub_menu.add_command(label = "Bonds", command = do_nothing)
invest_menu.add_cascade(label = "Buy", menu = buy_sub_menu)

#Adds submenu to Selling: 
sell_sub_menu = tk.Menu(menubar, tearoff = 0)
sell_sub_menu.add_command(label = "Stocks", command = do_nothing)
sell_sub_menu.add_command(label = "Bonds", command = do_nothing)
invest_menu.add_cascade(label = "Sell", menu = sell_sub_menu)

#Root configuration for menu bar
root.config(menu = menubar)

#Mainloop at the end
root.mainloop()

