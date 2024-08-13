class animal():

    def __init__(self,eso,tam,hab,alm):
    
        self.especie=eso
        self.size = tam
        self.habt= hab
        self.alim= alm

    def dezpl(self):
        print("el animal se esta dezplasando")

    def alimn(self):
        print("el animal se esta alimentando")


class paloma(animal):
    def __init__(self, eso, tam, hab, alm,sexo, color):
        super().__init__(eso, tam, hab, alm)
        self.sexo=sexo
        self.color=color
    def dezpl(self):
        print ("la paloma se esta desplazando")
    def volar(self):
        print("la paloma empezo a volar")
    def cnido(self):
        pass

paloma1=paloma("Ala blanca ", "pequena","cuidad","Omnivora","Hembra","negra y blanca")
paloma1.dezpl()
paloma1.volar()