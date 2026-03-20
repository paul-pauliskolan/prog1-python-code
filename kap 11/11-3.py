def get_user_info():
    # Hämtar användarens namn och ett tal
    name = input("Vad heter du? ")
    number = int(input("Skriv ett tal: "))
    return name, number


def calculate_double(number):
    # Beräknar talet gånger två
    return number * 2


def print_result(name, result):
    # Skriver ut resultatet till användaren
    print(f"Hej {name}")
    print(f"Ditt tal gånger två är {result}")


# Huvudprogram
name, number = get_user_info()
result = calculate_double(number)
print_result(name, result)