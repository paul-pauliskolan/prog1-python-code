import tkinter as tk
total = 0
def add_cost():
	global total
	try:
		cost = int(entry.get())
		total = total + cost
		result_label.config(text=f"Totalt: {total} kr")
	except:
		result_label.config(text="Fel inmatning")
window = tk.Tk()
window.title("Budget")
label = tk.Label(window, text="Ange kostnad i kronor:")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Lägg till kostnad", command=add_cost)
button.pack()
result_label = tk.Label(window, text="Totalt: 0 kr")
result_label.pack()
window.mainloop()
