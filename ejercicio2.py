try:
   numeros = int(input("solicite un numero impar emtre los 200 y 400 "))
   if numeros % 2 == 0 and 200 <= numeros <= 400:
       print("El número es par es 394 .")
   else:
       print("El número es impar .")
except ValueError:
   print("Por favor, introduce un número válido. el numero debe ser entre los 200 y 400")
