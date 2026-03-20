import tkinter as tk
from tkinter import ttk

# Skapa fönster
window = tk.Tk()
window.title("Test av Combobox")
window.geometry("300x200")

# Funktion som körs när man väljer något
def val_valt(event):
    print("Du valde:", combo.get())

# Skapa combobox
combo = ttk.Combobox(window, values=["A", "B"])
combo.pack(pady=20)

# Koppla event (när användaren väljer något)
combo.bind("<<ComboboxSelected>>", val_valt)

# Starta programmet
window.mainloop()