def hamta_film():
    namn = input("Skriv filmens namn: ")
    return namn

def hamta_langd():
    while True:
        try:
            langd = int(input("Skriv filmens längd i minuter: "))
            return langd
        except ValueError:
            print("Fel: skriv ett heltal")

def berakna_info(langd):
    timmar = langd / 60
    return timmar

def visa_resultat(namn, langd, timmar):
    print(f"Film: {namn}")
    print(f"Längd: {langd} minuter")
    print(f"Längd i timmar: {timmar:.2f}")

film = hamta_film()
langd = hamta_langd()
timmar = berakna_info(langd)
visa_resultat(film, langd, timmar)