# Facit till övning 10.3 Robusta program

while True:
    try:
        a = int(input("Skriv första talet: "))
        b = int(input("Skriv andra talet: "))

        if b == 0:
            print("Du kan inte dela med 0")
        else:
            result = a / b
            print(f"Resultatet är {result}")
            break

    except:
        print("Fel inmatning, försök igen")