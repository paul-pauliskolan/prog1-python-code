# Facit kapitel 11.5 Övningar


# Övning 1
# Förbättrade variabelnamn
number1 = 5
number2 = 10
summa = number1 + number2
print(summa)


# Övning 2
# fråga efter namn
name = input("Vad heter du? ")

# fråga efter ålder
age = int(input("Hur gammal är du? "))

# räkna ut ålder om 5 år
future_age = age + 5

# skriv ut resultat
print(f"Hej {name}")
print(f"Om fem år är du {future_age} år gammal")


# Övning 3
# mer läsbar kod
name = input("Vad heter du? ")
number = int(input("Skriv ett tal: "))

result = number * 2

print(f"Hej {name}")
print(result)


# Övning 4
# dela upp i funktioner
def greet(name):
    print(f"Hej {name}")

def double(number):
    return number * 2

name = input("Vad heter du? ")
number = int(input("Skriv ett tal: "))

greet(name)

result = double(number)
print(f"Ditt tal gånger två är {result}")


# Övning 5
# eget program med funktioner och kommentarer

# funktion som skriver ut hälsning
def greet(name):
    print(f"Hej {name}")

# funktion som räknar ut ålder om 10 år
def future_age(age):
    return age + 10

name = input("Vad heter du? ")
age = int(input("Hur gammal är du? "))

greet(name)

result = future_age(age)
print(f"Om tio år är du {result} år gammal")