import tkinter as tk

total = 0

def add_cost():
    global total
    try:
        cost = int(entry.get())
        total += cost
        result_label.config(text=f"Totalt: {total} kr")
        entry.delete(0, tk.END)
    except:
        result_label.config(text="Fel inmatning")

window = tk.Tk()

tk.Label(window, text="Kostnad").pack()
entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Lägg till", command=add_cost).pack()

result_label = tk.Label(window, text="Totalt: 0 kr")
result_label.pack()

window.mainloop()