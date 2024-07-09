
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
canvas.create_oval((60, 50, 100, 100), fill = 'magenta')
# left, top, right, bottom
canvas.create_line((0, 0, 100, 150), fill = 'blue')
# start_x, start_y, end_x, end_y
canvas.create_polygon((0,0, 100,200, 300,50))
# x1, y1, x2, y2, x3, y3

# run
app.mainloop()