import tkinter as tk

def convert():
    try:
        temp = float(entry.get())

        if choice.get() == 1:
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.1f}°F")
        else:
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.1f}°C")

    except:
        result_label.config(text="Skriv ett giltigt tal")

window = tk.Tk()
window.title("Temperaturomvandlare")

tk.Label(window, text="Ange temperatur:").pack()
entry = tk.Entry(window)
entry.pack()

choice = tk.IntVar()
choice.set(1)

tk.Radiobutton(window, text="Celsius till Fahrenheit", variable=choice, value=1).pack()
tk.Radiobutton(window, text="Fahrenheit till Celsius", variable=choice, value=2).pack()

tk.Button(window, text="Omvandla", command=convert).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()