# Facit 12.3 Tkinter

import tkinter as tk

def say_hello():
    print("Hej")

window = tk.Tk()
window.title("Mitt GUI-program")

button = tk.Button(window, text="Klicka här", command=say_hello)
button.pack()

window.mainloop()