class Dispositivo:
    def __init__(self, tipo, valor, caracteristicas):
        self.tipo = tipo  # Celular, Tablet o Portátil
        self.valor = valor
        self.caracteristicas = caracteristicas
        self.marca = "PHR"
        self.origen = "Importado"
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.valor * 1.70

    def __str__(self):
        return (f"Tipo: {self.tipo}, Marca: {self.marca}, Origen: {self.origen}, "
                f"Valor: ${self.valor:.2f}, Precio de Venta: ${self.precio_venta:.2f}, "
                f"Características: {', '.join(self.caracteristicas)}")

def registrar_dispositivo():
    tipo = input("Introduce el tipo de dispositivo (Celular/Tablet/Portátil): ").capitalize()

    while True:
        try:
            valor = float(input("Introduce el valor del dispositivo: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el valor del dispositivo.")

    caracteristicas = []
    print("Introduce las 6 principales características del dispositivo:")
    for i in range(6):
        caracteristica = input(f"Característica {i+1}: ")
        caracteristicas.append(caracteristica)

    return Dispositivo(tipo, valor, caracteristicas)

def mostrar_dispositivos(dispositivos):
    print("\nDispositivos registrados en la tienda:")
    for dispositivo in dispositivos:
        print(dispositivo)

def main():
    dispositivos = []

    while True:
        opcion = input("\n¿Deseas registrar un nuevo dispositivo? (sí/no): ").lower()
        if opcion == "si":
            nuevo_dispositivo = registrar_dispositivo()
            dispositivos.append(nuevo_dispositivo)
        elif opcion == "no":
            break
        else:
            print("Opción no válida. Por favor, introduce 'sí' o 'no'.")

    mostrar_dispositivos(dispositivos)

if __name__ == "__main__":
    main()
