# Facit kapitel 6.9 Övningar


# Övning 1
# Skriv ut talen 1 till 10
for i in range(1, 11):
    print(i)


# Övning 2
# Skriv ut talen 1 till 20 och visa om de är jämna eller udda
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} är jämnt")
    else:
        print(f"{i} är udda")


# Övning 3
# Läs in 5 tal och räkna ut summan
total = 0

for i in range(5):
    number = int(input("Skriv ett tal: "))
    total = total + number

print(f"Summan är {total}")


# Övning 4
# Multiplikationstabell
number = int(input("Skriv ett tal: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")


# Övning 5
# Läs tal tills användaren skriver 0
while True:
    number = int(input("Skriv ett tal (0 för att avsluta): "))

    if number == 0:
        break

    print(f"Du skrev {number}")


# Övning 6
# Summera tal tills användaren skriver 0
total = 0

while True:
    number = int(input("Skriv ett tal (0 för att avsluta): "))

    if number == 0:
        break

    total = total + number

print(f"Summan är {total}")


# Övning 7
# Räkna hur många tal användaren skriver
count = 0

while True:
    number = int(input("Skriv ett tal (0 för att avsluta): "))

    if number == 0:
        break

    count = count + 1

print(f"Du skrev {count} tal")


# Övning 8
# FizzBuzz från 1 till 50
for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
