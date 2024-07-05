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

# Events can be lots of things, such as..
# (1) Keyboard inputs
# (2) Widgets getting changed
# (3) Widgets gets selected / unselected
# (4) Mouse click / motion / wheel. and so on

# I need to bind events to a widget --> Widget.bind(event, function)
# Format : <modifier-type-detail>

# events
app.bind('<Alt-KeyPress-a>', lambda event: print(event))

# run
app.mainloop()