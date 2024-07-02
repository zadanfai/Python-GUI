import tkinter as tk
from tkinter import ttk

def button_func():
    print('The button was pressed')

    # get the content of the entry
    input = entry.get()

    # update the label
    # label.config(text = input) 
    # either config or configure is working
    label['text'] = input

# window
app = tk.Tk()
app.title('Window and Widgets')
app.geometry('700x500')

# create widgets
teks = tk.Text(master = app)
teks.pack()

# ttk widgets
label = ttk.Label(master = app, text = 'This is a test')
label.pack(pady = 10)

# ttk entry
entry = ttk.Entry(master = app)
entry.pack()

# ttk button
button = ttk.Button(master = app, text = 'A button', command = button_func) # The command only call a function, so don't add () in it
button.pack(pady = 5)

# run
app.mainloop()