import tkinter as tk
from tkinter import ttk


def on_start():
    print("started")

console_messages = []

for i in range(100):
    console_messages.append("zzzzzzz")


window = tk.Tk()

notebook = ttk.Notebook(window)

main_tab = tk.Frame(notebook)
console = tk.Frame(notebook)
analytics = tk.Frame(notebook)

notebook.add(main_tab, text="main tab")
notebook.add(console, text="console")
notebook.add(analytics, text="analytics")
notebook.pack(expand=True, fill=tk.BOTH)

canvas = tk.Canvas(console)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(console, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

inside_console = tk.Frame(canvas)

canvas.create_window((0, 0), window=inside_console, anchor="nw")


button = tk.Button(main_tab, text="start", command=on_start, font=("cosmic sans", 30))
button.pack()

for message in console_messages:
    m = tk.Label(inside_console, text=message)
    m.pack()

canvas.update_idletasks()

window.mainloop()