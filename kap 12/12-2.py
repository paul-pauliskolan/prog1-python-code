# Facit 12.2 Textbaserade menyer

name = input("Vad heter du? ")

while True:
    print("1. Skriv ut ditt namn")
    print("2. Räkna ut ett tal gånger 3")
    print("3. Avsluta")

    choice = input("Välj ett alternativ: ")

    if choice == "1":
        print(f"Ditt namn är {name}")

    elif choice == "2":
        number = int(input("Skriv ett tal: "))
        print(f"Resultatet är {number * 3}")

    elif choice == "3":
        print("Programmet avslutas")
        break

    else:
        print("Ogiltigt val")