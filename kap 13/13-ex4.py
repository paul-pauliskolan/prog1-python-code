import tkinter as tk
from tkinter import ttk

def save_note():
    content = text.get("1.0", tk.END).strip()
    category = combo.get()

    if agree.get():
        tree.insert("", tk.END, values=(category, content[:20]))
        text.delete("1.0", tk.END)
        result_label.config(text="Anteckning sparad")
    else:
        result_label.config(text="Du måste godkänna")

def open_window():
    new = tk.Toplevel(window)
    tk.Label(new, text="Hjälpfönster").pack()

window = tk.Tk()
window.title("Anteckningsapp")

# MENU
menu = tk.Menu(window)
window.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Arkiv", menu=file_menu)
file_menu.add_command(label="Nytt fönster", command=open_window)
file_menu.add_command(label="Avsluta", command=window.quit)

# NOTEBOOK
notebook = ttk.Notebook(window)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text="Skriv")
notebook.add(tab2, text="Lista")
notebook.pack()

# TAB 1
frame = tk.LabelFrame(tab1, text="Ny anteckning")
frame.pack(padx=10, pady=10)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(frame, height=5, yscrollcommand=scroll.set)
text.pack()

scroll.config(command=text.yview)

combo = ttk.Combobox(tab1, values=["Skola", "Jobb", "Privat"])
combo.pack()

agree = tk.BooleanVar()
tk.Checkbutton(tab1, text="Spara anteckning", variable=agree).pack()

tk.Button(tab1, text="Spara", command=save_note).pack()

result_label = tk.Label(tab1)
result_label.pack()

# TAB 2 (TREEVIEW)
tree = ttk.Treeview(tab2, columns=("Kategori", "Text"), show="headings")
tree.heading("Kategori", text="Kategori")
tree.heading("Text", text="Text")

tree.pack()

window.mainloop()