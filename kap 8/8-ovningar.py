# Facit kapitel 8.7 Övningar


# Övning 1
def greet(name):
    print(f"Hej {name}")


greet("Anna")


# Övning 2
def square(number):
    return number * number


result = square(4)
print(result)


# Övning 3
def add(a, b):
    return a + b


result = add(3, 5)
print(f"Summan är {result}")


# Övning 4
def age_in_five_years(age):
    return age + 5


age = int(input("Hur gammal är du? "))
future_age = age_in_five_years(age)

print(f"Om fem år är du {future_age} år gammal")


# Övning 5
def area(width, height):
    return width * height


width = int(input("Ange bredd: "))
height = int(input("Ange höjd: "))

result = area(width, height)

print(f"Arean är {result}")


# Övning 6
def greet(name):
    print(f"Hej {name}")


def double(number):
    return number * 2


name = input("Vad heter du? ")
number = int(input("Skriv ett tal: "))

greet(name)

result = double(number)

print(f"Det dubbla är {result}")
