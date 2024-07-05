import tkinter as tk
from tkinter import ttk


# im creating a function that will show us the location of the pointer in the app
def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# window
app = tk.Tk()
app.geometry('600x500')
app.title('Event Binding')

# widget
text = tk.Text(app)
text.pack()

entry = ttk.Entry(app)
entry.pack()

button = ttk.Button(app, text = 'A Button')
button.pack()

# Events can be lots of things, such as..
# (1) Keyboard inputs
# (2) Widgets getting changed
# (3) Widgets gets selected / unselected
# (4) Mouse click / motion / wheel. and so on

# I need to bind events to a widget --> Widget.bind(event, function)
# Format : <modifier-type-detail>

# events
button.bind('<Alt-KeyPress-a>', lambda event: print(event))
app.bind('<Motion>', get_pos)

app.bind('<KeyPress>', lambda event: print(f'a button was presesd ({event.char})'))

# run
app.mainloop()