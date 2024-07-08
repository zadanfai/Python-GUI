
import tkinter as tk
from tkinter import ttk

# window
app = tk.Tk()
app.title('Combobox & Spinbox')
app.geometry('500x300')

# combobox

items = ('Ice cream', 'Pizza', 'Broccoli')
combo = ttk.Combobox(app)
combo['values'] = items
combo.pack()


# Both need to get a list of values
# Both can be connected to a Tkinter variables

# run
app.mainloop()