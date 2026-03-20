# Facit kapitel 7.7 Övningar


# Övning 1
numbers = [3, 7, 2, 9, 5]

print(numbers)
print(numbers[0])
print(numbers[-1])


# Övning 2
numbers = [3, 7, 2, 9, 5]

for number in numbers:
    print(number)


# Övning 3
numbers = [4, 6, 2, 8, 10]

total = 0

for number in numbers:
    total = total + number

print(f"Summan är {total}")


# Övning 4
numbers = [4, 6, 2, 8, 10]

total = 0

for number in numbers:
    total = total + number

average = total / len(numbers)

print(f"Medelvärdet är {average}")


# Övning 5
numbers = []

for i in range(5):
    number = int(input("Skriv ett tal: "))
    numbers.append(number)

print(numbers)


# Övning 6
numbers = [3, 8, 5, 12, 7, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)


# Övning 7
numbers = [3, 8, 5, 12, 7, 10]

count = 0

for number in numbers:
    if number > 5:
        count = count + 1

print(f"Antal tal större än 5 är {count}")
