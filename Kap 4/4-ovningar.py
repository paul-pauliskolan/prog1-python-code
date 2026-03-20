# Övning 1 Enkel beräkning
number1 = int(input("Skriv första talet: "))
number2 = int(input("Skriv andra talet: "))
summa = number1 + number2
skillnad = number1 - number2
produkt = number1 * number2
print(f"Summan är {summa}")
print(f"Skillnaden är {skillnad}")
print(f"Produkten är {produkt}")

# Övning 2 Medelvärde
number1 = float(input("Skriv första talet: "))
number2 = float(input("Skriv andra talet: "))
number3 = float(input("Skriv tredje talet: "))
average = (number1 + number2 + number3) / 3
print(f"Medelvärdet är {average}")

# Övning 3 Räkna ut area
length = float(input("Skriv längden: "))
width = float(input("Skriv bredden: "))
area = length * width
print(f"Arean är {area}")

# Övning 4 Temperatur
celsius = float(input("Skriv temperatur i Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperaturen i Fahrenheit är {fahrenheit}")

# Övning 5 Dubbel kontroll
number = int(input("Skriv ett tal: "))
print(number > 10 and number < 100)

# Övning 6 Största talet
number1 = int(input("Skriv första talet: "))
number2 = int(input("Skriv andra talet: "))
if number1 > number2:
  print(f"{number1} är störst")
else:
  print(f"{number2} är störst")