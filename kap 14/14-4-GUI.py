import tkinter as tk

def berakna():
    namn = entry_namn.get().strip()
    
    if namn == "":
        label_resultat.config(text="Fel: skriv ett filmnamn")
        return
    
    try:
        langd = int(entry_langd.get())
        
        if langd <= 0:
            label_resultat.config(text="Fel: längden måste vara större än 0")
            return
        
        timmar = langd // 60
        minuter = langd % 60
        
        resultat_text = (
            f"Film: {namn}\n"
            f"Längd: {langd} minuter\n"
            f"Tid: {timmar} tim {minuter} min"
        )
        
        label_resultat.config(text=resultat_text)
        
    except ValueError:
        label_resultat.config(text="Fel: skriv ett heltal för längden")

def rensa():
    entry_namn.delete(0, tk.END)
    entry_langd.delete(0, tk.END)
    label_resultat.config(text="")

root = tk.Tk()
root.title("Filminfo")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_namn = tk.Label(frame, text="Film:")
label_namn.grid(row=0, column=0, sticky="w")

entry_namn = tk.Entry(frame)
entry_namn.grid(row=0, column=1)

label_langd = tk.Label(frame, text="Längd (minuter):")
label_langd.grid(row=1, column=0, sticky="w")

entry_langd = tk.Entry(frame)
entry_langd.grid(row=1, column=1)

knapp_berakna = tk.Button(frame, text="Beräkna", command=berakna)
knapp_berakna.grid(row=2, column=0, pady=5)

knapp_rensa = tk.Button(frame, text="Rensa", command=rensa)
knapp_rensa.grid(row=2, column=1, pady=5)

label_resultat = tk.Label(frame, text="", justify="left")
label_resultat.grid(row=3, column=0, columnspan=2)

root.mainloop()