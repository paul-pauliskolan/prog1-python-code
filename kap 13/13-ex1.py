import tkinter as tk
from tkinter import ttk

filmer = []

def add_movie():
    name = entry_name.get().strip()
    length = entry_length.get().strip()
    genre = combo.get().strip()

    try:
        length = int(length)

        if name == "":
            result_label.config(text="Du måste skriva filmens namn")
            return

        filmer.append(length)
        listbox.insert(tk.END, f"{name} ({length} min) - {genre}")

        total_min = sum(filmer)
        timmar = total_min // 60
        minuter = total_min % 60
        medel = total_min / len(filmer)

        summary_label.config(
            text=f"Total tid: {total_min} min ({timmar} h {minuter} min)\nMedellängd: {medel:.1f} min"
        )

        result_label.config(text="Film tillagd")

        entry_name.delete(0, tk.END)
        entry_length.delete(0, tk.END)

    except ValueError:
        result_label.config(text="Fel inmatning - ange längd i siffror")

window = tk.Tk()
window.title("Filmlista")

tk.Label(window, text="Film").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Längd i minuter").pack()
entry_length = tk.Entry(window)
entry_length.pack()

combo = ttk.Combobox(window, values=["Action", "Drama", "Komedi"])
combo.pack()
combo.set("Action")

tk.Button(window, text="Lägg till", command=add_movie).pack()

listbox = tk.Listbox(window, width=40)
listbox.pack()

result_label = tk.Label(window, text="")
result_label.pack()

summary_label = tk.Label(window, text="Total tid: 0 min (0 h 0 min)\nMedellängd: 0 min")
summary_label.pack()

window.mainloop()