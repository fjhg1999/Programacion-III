# creamos una funcion con su respectiva formula para dar una respuesta solicitada
def es_positivo_cuatro_digitos(numero):
    return 1000 <= numero <= 9999

# Leer un número entero desde la entrada del usuario
numero = int(input("Introduce un número entero: "))

# Determinar si el número es positivo y tiene 4 dígitos
if es_positivo_cuatro_digitos(numero):
    print(f"El número {numero} es un número positivo de 4 dígitos.")
else:
    print(f"El número {numero} no es un número positivo de 4 dígitos.")
