
import tkinter as tk
from tkinter import ttk

# window
app = tk.Tk()
app.title('Combobox & Spinbox')
app.geometry('500x300')

# combobox

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

# Both need to get a list of values
# Both can be connected to a Tkinter variables

# run
app.mainloop()