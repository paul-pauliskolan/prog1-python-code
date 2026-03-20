# Facit till övning 9.6 Testa program

# 1 - Man kan testa programmet med olika åldrar.
# Till exempel 10, 18, 30 eller 65.

# 2 - Det är bra att testa flera värden för att kontrollera att programmet alltid fungerar korrekt.
# Då kan man upptäcka fel i beräkningar eller logik.

# 3 - Om användaren skriver text istället för ett tal uppstår ett fel.
# Programmet kraschar eftersom int() inte kan omvandla text till ett heltal.

age = int(input("Hur gammal är du? "))
future_age = age + 10
print(f"Om tio år är du {future_age} år gammal")