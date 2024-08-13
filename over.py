class empleado():
    def __init__(self,nombr,sueldo):
        self.nombr=nombr
        self.sueldo= sueldo

    def info(self):
        return(f"nombre del empleado :{self.nombr}\n sueldo : {self.sueldo}")
class Gerente(empleado):
    def __init__(self, nombr, sueldo,area):
        super().__init__(nombr, sueldo)
        self.area= area

    def info(self):
        infoem=super().info()
        print(f"{infoem} area: {self.area}")
    
gerente=Gerente("pepito",800, "ventas")
gerente.info()