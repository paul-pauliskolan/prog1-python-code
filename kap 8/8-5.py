# Facit övning 8.5 Strukturera program


def greet(name):
    print(f"Hej {name}")


def add(a, b):
    return a + b


name = input("Vad heter du? ")
greet(name)

result = add(4, 6)
print(f"Summan är {result}")
