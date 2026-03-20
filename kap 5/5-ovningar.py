# Facit kapitel 5.8 Övningar


# Övning 1
age = int(input("Hur gammal är du? "))

if age < 13:
    print("Barn")
elif age <= 19:
    print("Tonåring")
else:
    print("Vuxen")


# Övning 2
number = int(input("Skriv ett tal: "))

if number > 0:
    print("Talet är positivt")
elif number < 0:
    print("Talet är negativt")
else:
    print("Talet är noll")


# Övning 3
number = int(input("Skriv ett tal: "))

if number % 2 == 0:
    print("Talet är jämnt")
else:
    print("Talet är udda")


# Övning 4
name = input("Vad heter du? ")
age = int(input("Hur gammal är du? "))

print(f"Hej {name}")

if age >= 18:
    print("Du är myndig")
else:
    print("Du är inte myndig")


# Övning 5
score = int(input("Hur många poäng fick du på provet? "))

if score < 50:
    print("Underkänt")
elif score < 80:
    print("Godkänt")
else:
    print("Mycket bra")


# Övning 6
age = int(input("Hur gammal är du? "))
student = input("Har du studentkort (ja/nej)? ")

if age < 20 or student == "ja":
    print("Rabatt beviljad")
else:
    print("Ingen rabatt")


# Övning 7
number = int(input("Skriv ett tal: "))

if number % 5 == 0:
    print("Delbart med 5")
else:
    print("Inte delbart med 5")


# Övning 8
temperature = int(input("Ange temperatur: "))

if temperature < 10:
    print("Kallt")
elif temperature <= 20:
    print("Lagom")
else:
    print("Varmt")
