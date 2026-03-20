# Facit till övning 10.2 Hantera felaktig input

while True:
    try:
        number = int(input("Skriv ett tal: "))
        print(number * 2)
        break
    except:
        print("Fel inmatning, försök igen")