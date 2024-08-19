# se crea la clase para almacenar datos sobre cada vehiculo
class Auto:
    def __init__(self, marca, modelo, tipo, valor, ruedas, pasajeros):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo  # Nacional o Importado
        self.valor = valor
        self.ruedas = ruedas
        self.pasajeros = pasajeros
        self.precio_venta = self.calcular_precio_venta()
# se calcula su precio tomando su valor *1.40
    def calcular_precio_venta(self):
        return self.valor * 1.40
# str ayuda para almacenar llamar los datos almacenada de cada vehiculo y para devolverlos a la imprecion del programa
    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: {self.tipo}, "
                f"Valor: ${self.valor:.2f}, Precio de Venta: ${self.precio_venta:.2f}, "
                f"Ruedas: {self.ruedas}, Pasajeros: {self.pasajeros}")
# se introducen los datos para almacenarlos
def registrar_auto():
    marca = input("Introduce la marca del auto: ")
    modelo = input("Introduce el modelo del auto: ")
    tipo = input("Introduce el tipo del auto (Nacional/Importado): ").capitalize()
# se crea un bucle para cada valor del auto para que el ususario solo agrege datos validos de cada uno
    while True:
        try:
            valor = float(input("Introduce el valor del auto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el valor del auto.")

    while True:
        try:
            ruedas = int(input("Introduce el número de ruedas del auto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para las ruedas del auto.")

    while True:
        try:
            pasajeros = int(input("Introduce la cantidad de pasajeros del auto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para la cantidad de pasajeros.")

    return Auto(marca, modelo, tipo, valor, ruedas, pasajeros)
# se imprimen los datos del array para mostrarlos cuando el usuario toca la opcion de salir
def mostrar_autos(autos):
    print("\nAutos registrados en el concesionario:")
    for auto in autos:
        print(auto)

def main():
    autos = []

    while True:
        opcion = input("\n¿Deseas registrar un nuevo auto? (sí/no): ").lower()
        if opcion == "si":
            nuevo_auto = registrar_auto()
            autos.append(nuevo_auto)
        elif opcion == "no":
            break
        else:
            print("Opción no válida. Por favor, introduce 'sí' o 'no'.")

    mostrar_autos(autos)

if __name__ == "__main__":
    main()