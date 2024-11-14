numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "escribe un numero valido"

print("\nResultados de las operaciones:")
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)
