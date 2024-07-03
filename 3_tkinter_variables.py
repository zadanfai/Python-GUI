
# Here i wanna try to make the Label should always have the same text as Entry
# Im using stringvar to make them automatically updated

import tkinter as tk
from tkinter import ttk

# window
app = tk.Tk()
app.title = 'Tkinter Variables'
app.geometry('500x300')

# tkinter variables
string_var = tk.StringVar(value = 'Label')

# widgets
label = ttk.Label(master = app, text = 'Label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = app, textvariable = string_var)
entry.pack()

# run
app.mainloop()