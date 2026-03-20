# Facit kapitel 10.4 Övningar


# Övning 1
try:
    number = int(input("Skriv ett tal: "))
    print(number * 3)
except:
    print("Fel inmatning")


# Övning 2
while True:
    try:
        number = int(input("Skriv ett tal: "))
        print(number + 10)
        break
    except:
        print("Fel inmatning, försök igen")


# Övning 3
try:
    a = int(input("Skriv första talet: "))
    b = int(input("Skriv andra talet: "))
    print(a + b)
except:
    print("Fel inmatning")


# Övning 4
while True:
    try:
        a = int(input("Skriv första talet: "))
        b = int(input("Skriv andra talet: "))
        print(a * b)
        break
    except:
        print("Fel inmatning, försök igen")


# Övning 5
while True:
    try:
        number = int(input("Skriv ett tal: "))

        if number == 0:
            print("Du kan inte dela med 0")
        else:
            print(100 / number)
            break

    except:
        print("Fel inmatning, försök igen")


# Övning 6
while True:
    try:
        number = int(input("Skriv ett tal större än 0: "))

        if number > 0:
            print(number * 5)
            break
        else:
            print("Talet måste vara större än 0")

    except:
        print("Fel inmatning, försök igen")