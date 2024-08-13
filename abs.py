from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def sonido(self):
        pass
class Perro(Animal):

    def __init__(self):
        self.nombre= " ese culo"
    def sonido(self):
        return (f" el {self.nombre} bota kk")
    
perro=Perro()
print(perro.sonido())
