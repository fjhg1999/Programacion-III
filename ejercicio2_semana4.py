#se crea la clase para poder agregar las datos de los productos
class Producto:
    def __init__(self, nombre, tipo, precio_costo):
        self.nombre = nombre
        self.tipo = tipo
        self.precio_costo = precio_costo
        self.precio_venta = self.calcular_precio_venta()
#se calcula su precio de venta tomando en cuenta su mismo valor que agrega el usuario *1.30
    def calcular_precio_venta(self):
        return self.precio_costo * 1.30
# str nos sirve para devolver cada dato almacenado para poder imprimirlo en el resultado
    def __str__(self):
        return f"Producto: {self.nombre}, Tipo: {self.tipo}, Precio de Venta: ${self.precio_venta:.2f}"
# aqui es donde introducimos cada producto a la lista donde se guardara
def registrar_producto():
    nombre = input("Introduce el nombre del producto: ")
    tipo = input("Introduce el tipo del producto: ")
# iniciamos un bucle para que el usuario introdusca un valor valido para el precio del producto
    while True:
        try:
            precio_costo = float(input("Introduce el precio de costo del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio de costo.")
    
    return Producto(nombre, tipo, precio_costo)
# llamamos el array para que se muestre las lista de productos que se almacenaron
def mostrar_productos(productos):
    print("\nProductos disponibles para la venta:")
    for producto in productos:
        print(producto)

def main():
    productos = []

    # Precios de costo iniciales
    precio_cuaderno_50_hojas = 2.00
    precio_cuaderno_100_hojas = 3.50
    precio_lapiz_grafito = 0.50
    precio_lapiz_colores = 1.00

    # Crear productos iniciales
    productos.append(Producto("Cuaderno HOJITAS", "50 hojas", precio_cuaderno_50_hojas))
    productos.append(Producto("Cuaderno HOJITAS", "100 hojas", precio_cuaderno_100_hojas))
    productos.append(Producto("Lápiz RAYAS", "grafito", precio_lapiz_grafito))
    productos.append(Producto("Lápiz RAYAS", "colores", precio_lapiz_colores))

    while True:
        opcion = input("\n¿Deseas registrar un nuevo producto? (sí/no): ").lower()
        if opcion == "si":
            nuevo_producto = registrar_producto()
            productos.append(nuevo_producto)
        elif opcion == "no":
            break
        else:
            print("Opción no válida. Por favor, introduce 'sí' o 'no'.")

    mostrar_productos(productos)

if __name__ == "__main__":
    main()