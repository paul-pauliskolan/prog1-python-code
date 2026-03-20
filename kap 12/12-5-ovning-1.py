# Uppgift 1 - Dubbla och tredubbla

import tkinter as tk

def double():
    try:
        number = int(entry.get())
        label.config(text=f"{number * 2}")
    except:
        label.config(text="Skriv ett tal")

def triple():
    try:
        number = int(entry.get())
        label.config(text=f"{number * 3}")
    except:
        label.config(text="Skriv ett tal")

window = tk.Tk()
window.title("x2 och x3")

entry = tk.Entry(window)
entry.pack()

btn1 = tk.Button(window, text="x2", command=double)
btn1.pack()

btn2 = tk.Button(window, text="x3", command=triple)
btn2.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()