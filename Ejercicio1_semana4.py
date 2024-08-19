# inicia la clase perro para poder agregar los atributos del perro
# y tambien agregar las 8 caracteristicas de cada uno
class Perro:
    def __init__(self, nombre, peso, caracteristicas):
        self.nombre = nombre
        self.peso = peso
    # aqui agregamos las caracteristicas mencionadas
        self.caracteristicas = caracteristicas[:8]  # Limitar a 8 características
        self.estado = "no atendido"
        self.categoria = "grande" if peso > 10 else "pequeño"
# aqui cambiamos el estado del perro de no atendido a atendido
    def registrar(self):
        self.estado = "atendido"
#definimos str para que devuelva una presentacion en cadena de las informacion del perro incluyendo las caracteristicas
    def __str__(self):
        caracteristicas_str = ", ".join(self.caracteristicas)
        return f"Nombre: {self.nombre}, Peso: {self.peso}kg, Estado: {self.estado}, Categoría: {self.categoria}, Características: {caracteristicas_str}"
#creamos una lista vacia para almacenar los perros que vayamos ingresando
def main():
    perros = []
# creamos un bucle para que el usuario introduzca en nombre del perro junto a todas las caracteristicas hasta que el usuario decida salir se mostraran los resultados

    while True:
        nombre = input("Introduce el nombre del perro ('salir' para terminar): ")
        if nombre.lower() == "salir":
            break
 #el ingreso del peso se crea con float para permitir decimales       
        peso = float(input("Introduce el peso del perro en kg: "))
        
        caracteristicas = []
        print("Introduce hasta 8 características del perro (una por línea, 'done' para terminar):")
# dimencionamos un array para podre agregar las caracteristicas de cada perro
        for i in range(8):
            caracteristica = input(f"Característica {i+1}: ")
            if caracteristica.lower() == "done":
                break
            caracteristicas.append(caracteristica)
        
        perro = Perro(nombre, peso, caracteristicas)
        perro.registrar()
        perros.append(perro)
# imprimimos todos los datos almacenados en el objeto de perro sin importar la cantidad de perros ya que por eso creamos un array
    print("\nInformación de los perros registrados:")
    for perro in perros:
        print(perro)

if __name__ == "__main__":
    main()