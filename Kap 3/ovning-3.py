# Övning 1 Hälsningsprogram
name = input("Vad heter du? ")
print(f"Hej {name}")

# Övning 2 Ålder om tio år
age = int(input("Hur gammal är du? "))
future_age = age + 10
print(f"Om tio år är du {future_age} år gammal")

# Övning 3 Summan av två tal
number1 = int(input("Skriv första talet: "))
number2 = int(input("Skriv andra talet: "))
summa = number1 + number2
print(f"Summan är {summa}")

# Övning 4 Temperaturprogram
celsius = float(input("Skriv temperatur i Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperaturen i Fahrenheit är {fahrenheit}")

# Övning 5 Medelvärde
number1 = float(input("Skriv första talet: "))
number2 = float(input("Skriv andra talet: "))
number3 = float(input("Skriv tredje talet: "))
average = (number1 + number2 + number3) / 3
print(f"Medelvärdet är {average}")

# Övning 6 Största talet
number1 = int(input("Skriv första talet: "))
number2 = int(input("Skriv andra talet: "))
if number1 > number2:
 print(f"{number1} är störst")
else:
 print(f"{number2} är störst")