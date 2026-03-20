# Uppgift 2 - Gånger 5 med felhantering

import tkinter as tk

def multiply():
    try:
        number = int(entry.get())
        label.config(text=f"{number * 5}")
    except:
        label.config(text="Fel inmatning")

window = tk.Tk()
window.title("Gånger 5")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Beräkna", command=multiply)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()