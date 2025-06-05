# Programa que verifica si una cadena es palíndroma con manejo de excepciones

try:
    cadena = input("Ingrese una cadena:")
    if cadena == "":
        raise ValueError("La cadena no puede estar vacía.")
    cadena_sin_espacios = cadena.replace(" ", "").lower()
    if cadena_sin_espacios == cadena_sin_espacios[::-1]:
        print("Es una cadena palíndroma.")
    else:
        print("No es una cadena palíndroma.")
except ValueError as e:
    print(f"Error: {e}")
