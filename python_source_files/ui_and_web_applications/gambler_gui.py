"""
GUI for betting simulation
"""

import tkinter as tk
import pickle

from user import User
from gambler import betting

#Starts root
root = tk.Tk()
root.title('Betting Simulation')

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
    games_get = games.get()
    money_get = money.get()
    bet_get = bet.get()

    #Close new_game_window
    new_user_window.destroy()

    #Create global variables
    global user

    #Initialize user
    user = User(games = games_get, money = money_get, bet = bet_get)

    #CHECK
    print(f"You want to play {user.games} games.")
    print(f"\nYou have initial wealth {user.money} and bet {user.bet}.")


def new_user():
    #New window
    global new_user_window
    new_user_window = tk.Toplevel()
    new_user_window.title('New Simulation')
    
    #Size of widget
    new_user_window.geometry("400x300")
    
    #Create global variables
    global games
    global money
    global bet

    games = tk.StringVar() 
    money = tk.StringVar() 
    bet = tk.StringVar() 

    #Entry: number of games, money, and value of bet
    games_entry = tk.Entry(new_user_window, width = 30, textvariable = games)
    games_entry.grid(row = 0, column = 1, padx = 20)  
     
    money_entry = tk.Entry(new_user_window, width = 30, textvariable = money)
    money_entry.grid(row = 1, column = 1, padx = 20) 

    bet_entry = tk.Entry(new_user_window, width = 30, textvariable = bet)
    bet_entry.grid(row = 2, column = 1, padx = 20) 

    #Labels for entries
    games_label = tk.Label(new_user_window, text = "Number of games")
    games_label.grid(row = 0, column = 0)
    
    money_label = tk.Label(new_user_window, text = "Initial wealth")
    money_label.grid(row = 1, column = 0)   

    bet_label = tk.Label(new_user_window, text = "Value of each bet")
    bet_label.grid(row = 2, column = 0)  

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
    print(f"{user.games} SAVED.")


def load():
    """Loads objects"""
    with open('portfolio.pkl', 'rb') as input:
        obj = pickle.load(input)
    global user
    user = obj[0]

    #CHECK
    print(f"{user.games} LOADED.")


def start_simulation():
    position = betting(money = int(user.money), games = int(user.games), initial_bet = int(user.bet)) 
    cash_display.delete(0, "end")
    cash_display.insert(0, position[-1])


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

#Simulation menu
sim_menu = tk.Menu(menubar, tearoff = 0)
sim_menu.add_command(label = "Start", command = start_simulation)
menubar.add_cascade(label = "Simulation", menu = sim_menu)

#Display
current_frame = tk.LabelFrame(root, text = 'Simulation result')
current_frame.grid(row = 1, column = 1, \
sticky='W', padx = 5, pady = 10, ipadx = 100, ipady = 30)

fin_position_label = tk.Label(current_frame, text = "Financial Position").grid(row = 0, column = 0)
cash_display = tk.Entry(current_frame, width = 10, borderwidth = 5)
cash_display.grid(row = 1, column = 1)
cash_label = tk.Label(current_frame, text = "Wealth").grid(row = 1, column = 0)

#Root configuration for menu bar
root.config(menu = menubar)

#Mainloop at the end
root.mainloop()