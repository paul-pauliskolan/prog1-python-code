# Uppgift 3 - Ålder om 5 år

import tkinter as tk

def calculate_age():
    try:
        age = int(entry.get())
        label.config(text=f"Om 5 år är du {age + 5} år")
    except:
        label.config(text="Skriv ett tal")

window = tk.Tk()
window.title("Åldersprogram")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Beräkna", command=calculate_age)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()