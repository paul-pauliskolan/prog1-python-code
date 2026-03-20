# Facit övning 7.5 Bearbeta data

numbers = [4, 6, 2, 8, 10]

# Räkna ut summan
total = 0

for number in numbers:
    total += number
    # total = total + number


# Räkna ut medelvärdet
average = total / len(numbers)

# Skriv ut resultaten
print(f"Summan är {total}")
print(f"Medelvärdet är {average}")
