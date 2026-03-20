import tkinter as tk
from tkinter import ttk

def add_movie():
    name = entry_name.get()
    length = entry_length.get()
    genre = combo.get()

    try:
        length = int(length)
        listbox.insert(tk.END, f"{name} ({length} min) - {genre}")
    except:
        result_label.config(text="Fel inmatning")

window = tk.Tk()
window.title("Filmlista")

tk.Label(window, text="Film").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Längd").pack()
entry_length = tk.Entry(window)
entry_length.pack()

combo = ttk.Combobox(window, values=["Action", "Drama", "Komedi"])
combo.pack()

tk.Button(window, text="Lägg till", command=add_movie).pack()

listbox = tk.Listbox(window)
listbox.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()