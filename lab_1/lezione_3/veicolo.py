
class Veicolo:	
    velocita = 0
    def __init__(self, marca, modello, anno):
        self.marca      = marca
        self.modello    = modello
        self.anno       = anno

    def __str__(self):
        return f"""Questi sono i dati del Veicolo:
                marca       : {self.marca}
                modello     : {self.modello}
                anno        : {self.anno}
                velocità    : {self.velocita}"""
    
    def accellerare(self):
        self.velocita += 5

    def frenare(self):
        self.velocita -= 5

    def get_speed(self):
        return self.velocita

class Auto(Veicolo):
    
    def __init__(self,marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def __str__(self):
        return super().__str__() + f"""
                numero_porte: {self.numero_porte}"""
    
class Moto(Veicolo):
    
    def __init__(self,marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f"""
                tipo        : {self.tipo}"""
    
# veicolo = Veicolo("Opel", "Mokka", 2017)
# print(veicolo)
# for i in range(10):
#     veicolo.accellerare()
# print(veicolo.get_speed())
# for i in range(10):
#     veicolo.frenare()
# print(veicolo)

auto = Auto("Opel", "Mokka", 2017, 4)
moto = Moto("KTM", "A mammt", 2019, "sportiva")
print(auto)
print(moto)
