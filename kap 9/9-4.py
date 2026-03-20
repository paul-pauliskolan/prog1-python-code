# Facit till övning 9.4 Läsa felmeddelanden

# 1 - Felet som uppstår är ett TypeError.
# 2 - Felet uppstår eftersom input() ger en text (str) men programmet försöker lägga till talet 5.
# 3 - Man måste omvandla texten till ett heltal med int().

age = int(input("Hur gammal är du? "))
result = age + 5
print(result)