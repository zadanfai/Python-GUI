
import tkinter as tk
from tkinter import ttk

# setup
app = tk.Tk()
app.title('Basic Paint App')
app.geometry('600x400')

# canvas
canvas = tk.Canvas(app, bg = 'white')
canvas.pack(pady = 10)

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill = 'black')

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

# widget
label = tk.Label(app, text = 'Scroll to adjust brush size')
label.pack()

# run
app.mainloop()