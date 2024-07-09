
import tkinter as tk
from tkinter import ttk

# setup
app = tk.Tk()
app.geometry('600x400')
app.title('canvas')

# canvas
canvas = tk.Canvas(app, bg = 'white')
canvas.pack()

canvas.create_rectangle((50, 20, 100, 200), fill = 'red', width = 10, dash = (1,2), outline = 'green') 
canvas.create_oval((200, 0, 300, 100), fill = 'magenta')
canvas.create_arc(
    (200, 0, 300, 100), 
    fill = 'red', 
    start = 45, 
    extent = 180, 
    style = tk.CHORD, 
    outline = 'yellow', 
    width = 10) # same as oval, start = start degrees, extent = adding degrees from start degrees
# left, top, right, bottom

canvas.create_line((0, 0, 100, 150), fill = 'blue')
# start_x, start_y, end_x, end_y

# canvas.create_polygon((0,0, 100,200, 300,50))
# x1, y1, x2, y2, x3, y3

canvas.create_text((100, 200), text = 'This is testing text', fill = 'green')

canvas.create_window((100, 100), window = ttk.Button(app, text = 'This is text in canvas'))



# run
app.mainloop()