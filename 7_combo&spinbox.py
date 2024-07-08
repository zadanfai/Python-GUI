
import tkinter as tk
from tkinter import ttk

# window
app = tk.Tk()
app.title('Combobox & Spinbox')
app.geometry('500x300')

# Combobox

items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value = items[0]) # To set value for the first place
combo = ttk.Combobox(app, textvariable= food_string)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

# events for combobox

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

# combobox label

combo_label = ttk.Label(app, text = 'a label')
combo_label.pack()


# Spinbox

spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    app, 
    from_ = 3, 
    to = 20, 
    increment = 3, 
    command = lambda: print(spin_int.get()),
    textvariable = spin_int
) 
# increment = jump values, from_ & to = list of values to spin
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['value'] = (1,2,3,4,5) 
spin.pack()

# Both need to get a list of values
# Both can be connected to a Tkinter variables

# run
app.mainloop()