
# There are 3 major kinds of buttons
# Buttons, chekButtons, and radioButtons

import tkinter as tk
from tkinter import ttk

# setup
app = tk.Tk()
app.title('buttons')
app.geometry('500x300')

# button

def button_func():
    print('This is basic button')

# button = ttk.Button(app, text= 'This is button', command = lambda: print('This is another way using lambda')) # the first argument is gonna be the master

# Another way to assign button var..
# button_var = tk.StringVar(value = 'This way using stringvar')
# button = ttk.Button(app, text= 'A simple button', command = button_func, textvariable = button_var)

button = ttk.Button(app, text= 'This is button', command = button_func)
button.pack()


# Check button

check_var = tk.IntVar()
check = ttk.Checkbutton(
    app, 
    text = 'checkbox 1', 
    command = lambda: print(check_var.get()),  # getting boolean in return
    variable = check_var,
    onvalue = 10, # getting assigned value in return
    offvalue = 5 ) # getting assigned value in return
check.pack()

# check button doesnt have textvariable


# Radio button

def radiobutton_func():
    print(radio_var.get())

radio_var = tk.StringVar() # variable dtype based on radio button value
radio1 = ttk.Radiobutton(
    app, 
    text = 'radiobutton 1', 
    value = 'radio1',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    app, 
    text = 'radiobutton 2', 
    value = 'radio2',
    variable = radio_var,
    command = radiobutton_func)
radio2.pack()

# if u dont assign the value its gonna be 0, and if u assign the same value tkinter would get confused

# run
app.mainloop()