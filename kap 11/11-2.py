# Frågar användaren efter sitt namn och sparar det i variabeln name
name = input("Vad heter du? ")

# Frågar efter användarens ålder och omvandlar svaret till ett heltal (int)
age = int(input("Hur gammal är du? "))

# Beräknar hur gammal användaren kommer vara om 10 år
future_age = age + 10

# Skriver ut en hälsning med användarens namn
print(f"Hej {name}")

# Skriver ut hur gammal användaren kommer vara om 10 år
print(f"Om tio år är du {future_age} år gammal")