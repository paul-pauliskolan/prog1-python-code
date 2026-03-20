# Facit till övning 14.6
# Dokumentation av filmprogrammet

# Beskrivning av programmet:
# Programmet tar emot ett filmnamn och en längd i minuter.
# Sedan räknar programmet om tiden till timmar och minuter.
# Resultatet visas i ett grafiskt fönster.
# Programmet visar också felmeddelanden om användaren skriver fel.

import tkinter as tk

# Denna funktion hämtar användarens inmatning,
# kontrollerar att värdena är korrekta
# och visar resultatet i fönstret.
def berakna():
    namn = entry_namn.get().strip()

    # Kontroll av tomt filmnamn
    if namn == "":
        label_resultat.config(text="Fel: skriv ett filmnamn")
        return

    try:
        # Försöker omvandla längden till heltal
        langd = int(entry_langd.get())

        # Kontroll av ogiltigt värde
        if langd <= 0:
            label_resultat.config(text="Fel: längden måste vara större än 0")
            return

        # Räknar om minuter till timmar och minuter
        timmar = langd // 60
        minuter = langd % 60

        # Visar resultatet på flera rader
        resultat_text = (
            f"Film: {namn}\n"
            f"Längd: {langd} minuter\n"
            f"Tid: {timmar} tim {minuter} min"
        )

        label_resultat.config(text=resultat_text)

    except ValueError:
        # Visas om användaren inte skriver ett heltal
        label_resultat.config(text="Fel: skriv ett heltal för längden")

# Denna funktion rensar inmatningsfälten och resultatet
def rensa():
    entry_namn.delete(0, tk.END)
    entry_langd.delete(0, tk.END)
    label_resultat.config(text="")

# Skapar programmets huvudfönster
root = tk.Tk()
root.title("Filminfo")

# Skapar en ram som håller ihop innehållet i fönstret
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Etikett och inmatningsfält för filmnamn
label_namn = tk.Label(frame, text="Film:")
label_namn.grid(row=0, column=0, sticky="w")

entry_namn = tk.Entry(frame)
entry_namn.grid(row=0, column=1)

# Etikett och inmatningsfält för filmens längd
label_langd = tk.Label(frame, text="Längd (minuter):")
label_langd.grid(row=1, column=0, sticky="w")

entry_langd = tk.Entry(frame)
entry_langd.grid(row=1, column=1)

# Knapp som startar beräkningen
knapp_berakna = tk.Button(frame, text="Beräkna", command=berakna)
knapp_berakna.grid(row=2, column=0, pady=5)

# Knapp som rensar innehållet
knapp_rensa = tk.Button(frame, text="Rensa", command=rensa)
knapp_rensa.grid(row=2, column=1, pady=5)

# Label där resultat eller felmeddelanden visas
label_resultat = tk.Label(frame, text="", justify="left")
label_resultat.grid(row=3, column=0, columnspan=2)

# Startar programmets GUI-loop
root.mainloop()

# Hur användaren använder programmet:
# 1. Skriv filmens namn i första rutan.
# 2. Skriv filmens längd i minuter i andra rutan.
# 3. Klicka på knappen Beräkna.
# 4. Läs resultatet i fönstret.
# 5. Klicka på Rensa om du vill börja om.