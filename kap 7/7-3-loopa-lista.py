# Facit övning 7.3 Loopar över listor

numbers = [2, 4, 6, 8, 10]

# 1 Skriv ut alla tal i listan
for number in numbers:
    print(number)

# 2 Skriv ut varje tal multiplicerat med 3
for number in numbers:
    print(number * 3)

# 3 Skriv ut summan av alla tal i listan
total = 0

for number in numbers:
    total = total + number

print(f"Summan är {total}")
