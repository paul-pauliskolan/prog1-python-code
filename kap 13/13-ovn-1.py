import tkinter as tk
from tkinter import ttk

def add_movie():
    name = entry_name.get()
    length = entry_length.get()
    genre = combo.get()

    if favorite.get():
        fav = "⭐"
    else:
        fav = ""

    try:
        length = int(length)
        tree.insert("", tk.END, values=(name, length, genre, fav))
    except:
        result_label.config(text="Fel inmatning")

def open_info():
    new = tk.Toplevel(window)
    tk.Label(new, text="Filmappen sparar dina filmer").pack()

window = tk.Tk()
window.title("Filmregister")

# MENU
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Meny", menu=file_menu)
file_menu.add_command(label="Info", command=open_info)
file_menu.add_command(label="Avsluta", command=window.quit)

# INPUT
tk.Label(window, text="Film").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Längd").pack()
entry_length = tk.Entry(window)
entry_length.pack()

tk.Label(window, text="Genre").pack()
combo = ttk.Combobox(window, values=["Action", "Drama", "Komedi"])
combo.pack()

favorite = tk.BooleanVar()
tk.Checkbutton(window, text="Favorit", variable=favorite).pack()

tk.Button(window, text="Lägg till", command=add_movie).pack()

# TABELL
tree = ttk.Treeview(window, columns=("Namn", "Längd", "Genre", "Fav"), show="headings")

tree.heading("Namn", text="Namn")
tree.heading("Längd", text="Min")
tree.heading("Genre", text="Genre")
tree.heading("Fav", text="⭐")

tree.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()