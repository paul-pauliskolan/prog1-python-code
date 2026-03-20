# Facit till övning 14.3
# Exempel på design med pseudokod och enkel struktur

# Program: Filmlista

# Design (pseudokod):

# Starta program
# Fråga användaren efter filmens namn
# Fråga användaren efter filmens längd
# Kontrollera att längden är ett heltal
# Spara informationen
# Visa filmens namn och längd
# Avsluta program



# Exempel på hur programmet kan implementeras:
film = input("Skriv filmens namn: ")

try:
    langd = int(input("Skriv filmens längd i minuter: "))
    print("Film sparad")
    print(f"Namn: {film}")
    print(f"Längd: {langd} minuter")
except ValueError:
    print("Fel: Du måste skriva ett heltal.")