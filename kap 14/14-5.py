# Facit till övning 14.5
# Testning av filmprogrammet

# Testfall 1
# Inmatning:
# Filmnamn: Interstellar
# Längd: 169
#
# Förväntat resultat:
# Programmet ska visa filmens namn
# Programmet ska visa 169 minuter
# Programmet ska visa 2 tim 49 min
#
# Vad som faktiskt händer:
# Programmet visar filmens namn korrekt
# Programmet visar längden korrekt
# Programmet visar tiden 2 tim 49 min
#
# Behöver något ändras:
# Nej, testet fungerar som det ska

# Testfall 2
# Inmatning:
# Filmnamn:
# Längd: 120
#
# Förväntat resultat:
# Programmet ska visa ett felmeddelande om att filmnamn saknas
#
# Vad som faktiskt händer:
# Programmet visar felmeddelandet "Fel: skriv ett filmnamn"
#
# Behöver något ändras:
# Nej, detta fungerar som det ska

# Testfall 3
# Inmatning:
# Filmnamn: Avatar
# Längd: abc
#
# Förväntat resultat:
# Programmet ska visa ett felmeddelande om att längden måste vara ett heltal
#
# Vad som faktiskt händer:
# Programmet visar felmeddelandet "Fel: skriv ett heltal för längden"
#
# Behöver något ändras:
# Nej, detta fungerar som det ska

# Testfall 4
# Inmatning:
# Filmnamn: Dune
# Längd: -5
#
# Förväntat resultat:
# Programmet ska visa ett felmeddelande om att längden måste vara större än 0
#
# Vad som faktiskt händer:
# Programmet visar felmeddelandet "Fel: längden måste vara större än 0"
#
# Behöver något ändras:
# Nej, detta fungerar som det ska

# Slutsats
# Programmet klarar både korrekta och felaktiga inmatningar.
# Testningen visar att programmet fungerar som tänkt.
#
# Det går ändå att förbättra programmet ännu mer, till exempel genom att:
# - lägga till en knapp för att avsluta programmet
# - göra fönstret snyggare
# - kontrollera att filmnamnet inte bara innehåller mellanslag