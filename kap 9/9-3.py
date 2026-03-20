# 1 - Om användaren skriver 0, kraschar programmet med ett felmeddelande på grund av division med noll.
# 2 - Felet uppstår eftersom division med noll inte är tillåten.
# 3 - Man kan undvika felet genom att kontrollera om talet är noll innan divisionen.

number = int(input("Skriv ett tal: "))

if number == 0:
    print("Division med noll är inte tillåten.")
else:
    result = 100 / number
    print(result)
