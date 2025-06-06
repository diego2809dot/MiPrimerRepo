////// programa que visualiza en pantalla  numeros multiplos de 5 comprendidos entre 10 y 200


while True:
        n = int(input("Introduce un número múltiplo de 5 comprendido entre 10 y 200: "))
        if n % 5 == 0 and 10 <= n <= 200:
            break
        else:
            print("El número debe ser un múltiplo de 5 y estar entre 10 y 200.") 
    if n % 5 != 0:
        raise ValueError("El número debe ser un múltiplo de 5.")
    if n % 10 == 0:
        print("El número es un múltiplo de 10.")
    if n == 200:
        print("El número es 200.")  
else: 
 print( "los numeros ingresados no se encuentran  en el rango permitido")


