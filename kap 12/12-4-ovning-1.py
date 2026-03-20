# Uppgift 1 - Hälsningsprogram

import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hej {name}")

window = tk.Tk()
window.title("Hälsningsprogram")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Säg hej", command=greet)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()