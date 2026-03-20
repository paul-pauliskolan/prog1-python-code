import tkinter as tk
def add_movie():
	name = entry_name.get()
	try:
		length = int(entry_length.get())
		result_label.config(text=f"Filmen {name} är {length} minuter lång")
	except:
		result_label.config(text="Skriv en giltig längd")
window = tk.Tk()
window.title("Filmlista")
label_name = tk.Label(window, text="Filmens namn:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()
label_length = tk.Label(window, text="Längd i minuter:")
label_length.pack()
entry_length = tk.Entry(window)
entry_length.pack()
button = tk.Button(window, text="Lägg till film", command=add_movie)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
