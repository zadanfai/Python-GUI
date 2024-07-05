import tkinter as tk
from tkinter import ttk

# window
app = tk.Tk()
app.geometry('600x500')
app.title('Event Binding')

# widget
text = tk.Text(app)
text.pack()

entry = ttk.Entry(app)
entry.pack()

btn = ttk.Button(app, text = 'A Button')
btn.pack()

# events
app.bind('<Alt-KeyPress-a>', lambda event: print(event))

# run
app.mainloop()