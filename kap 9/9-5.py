# Facit till övning 9.5 Systematisk felsökning

# 1 - Felet är att Python räknar division före addition.
# Uttrycket a + b / 2 betyder därför a + (b / 2), vilket ger fel medelvärde.

# 2 - Man kan använda print() för att kontrollera värden i programmet.
# Till exempel kan man skriva ut variablerna innan beräkningen.

a = int(input("Skriv första talet: "))
b = int(input("Skriv andra talet: "))

print(a)
print(b)

# 3 - För att räkna ut medelvärdet korrekt måste man använda parenteser.
# Då räknas summan först och sedan divisionen.

average = (a + b) / 2

print(f"Medelvärdet är {average}")