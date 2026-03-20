# Uppgift 2 - Dubbla tal

import tkinter as tk

def double():
    try:
        number = int(entry.get())
        label.config(text=f"{number * 2}")
    except:
        label.config(text="Skriv ett tal")

window = tk.Tk()
window.title("Dubbla tal")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Dubbla", command=double)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()