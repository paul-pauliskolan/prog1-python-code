# Facit kapitel 9.7 Övningar


# Övning 1
# Fel: saknar + eller , i print
name = input("Vad heter du? ")
print("Hej " + name)


# Övning 2
# Fel: använder minus istället för plus
a = 8
b = 4
summa = a + b
print(summa)


# Övning 3
# Fel: division med noll kan krascha programmet
number = int(input("Skriv ett tal: "))

if number == 0:
    print("Division med noll är inte tillåten")
else:
    result = 50 / number
    print(result)


# Övning 4
# Fel: fel operatorordning
a = 10
b = 20
average = (a + b) / 2
print(average)


# Övning 5
# Fel: funktionen anropas inte
def greet(name):
    print(f"Hej {name}")

greet("Anna")


# Övning 6
# Fel: saknar kolon efter for
for i in range(5):
    print(i)