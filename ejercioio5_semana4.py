# Leer dos números desde la entrada del usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Determinar cuál es el mayor número
if numero1 > numero2:
    print(f"El mayor número es: {numero1}")
elif numero2 > numero1:
    print(f"El mayor número es: {numero2}")
else:
    print("Ambos números son iguales.")