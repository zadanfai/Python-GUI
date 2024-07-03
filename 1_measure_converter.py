import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    km_input = entry_int.get()
    mile_output = km_input * 0.62
    output_string.set(f'{mile_output} miles')

#window
window = ttk.Window(themename = 'darkly')
window.title('Measure Converter')
window.geometry('600x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack(pady = 10)

#input field
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', comman = convert)
entry.pack(side = 'left', padx = 5)
button.pack(side = 'left')
input_frame.pack(pady = 5)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 24', 
    textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()