# Facit övning 7.6 Program med listor

numbers = []

# Be användaren skriva fem tal
for i in range(5):
    number = int(input("Skriv ett tal: "))
    numbers.append(number)

# Räkna ut summan
total = 0

for number in numbers:
    total = total + number

# Skriv ut listan och summan
print(numbers)
print(f"Summan är {total}")
