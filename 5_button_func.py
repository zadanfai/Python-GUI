
# This one i wanna try to explore the function with arguments (inside a button)
# Previously i already solved Command = lambda:print(arguments)

import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('Button was pressed')
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print('Button was pressed')
        print(parameter.get())
    return inner_func
# setup
app = tk.Tk()
app.title('buttons, function and arguments')
app.geometry('500x300')

# widgets

entry_string = tk.StringVar(value = 'Test')
entry = ttk.Entry(app, textvariable = entry_string)
entry.pack()

# button = ttk.Button(
#     app, 
#     text = 'Button', 
#     command = button_func(entry_string)) 

# The command is going to executed and returning none, cause i dont put returning value in the function
# theres 2 ways to fix this issue: 

# (1) is using lambda like i basically using all the time, this lambda function by default is not being called 
# button = ttk.Button(
#     app, 
#     text = 'Button', 
#     command = lambda: button_func(entry_string)) 

# (2) is creating a nested function
button = ttk.Button(app, text = 'Button', command = outer_func(entry_string))

button.pack()

# run
app.mainloop()