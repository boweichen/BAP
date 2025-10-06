"""
Menu bar
"""

import tkinter as tk

#Starts root
root = tk.Tk()
root.title('Menu bars')

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


"""
Menu bar   
"""
menubar = tk.Menu(root)

#File menu
file_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label = "New", command = do_nothing)
file_menu.add_command(label = "Save", command = do_nothing)
file_menu.add_command(label = "Load", command = do_nothing)
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

