# Facit övning 8.6 Större program


def greet(name):
    print(f"Hej {name}")


def square(number):
    return number * number


def double(number):
    return number * 2


name = input("Vad heter du? ")

greet(name)

number = int(input("Skriv ett tal: "))

square_result = square(number)
double_result = double(number)

print(f"Kvadraten är {square_result}")
print(f"Det dubbla är {double_result}")
