# Programa que verifica si un año es bisiesto con manejo de excepciones

try:
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"El año {año} es bisiesto.")
    else:
        print(f"El año {año} no es bisiesto.")
except ValueError:
    print("Error: Ingrese un año válido (número entero).")
