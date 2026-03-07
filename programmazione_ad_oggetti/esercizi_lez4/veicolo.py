
class Veicolo:	
    velocita = 0
    def __init__(self, marca, modello, anno):
        self.marca      = marca
        self.modello    = modello
        self.anno       = anno

    def __str__(self):
        return f"""Questi sono i dati del Veicolo:
                modello     : {self.modello}
                marca       : {self.marca}
                anno        : {self.anno}
                velocità    : {self.velocita}"""
    
    def accellerare(self):
        self.velocita += 5

    def frenare(self):
        self.velocita -= 5

    def get_speed(self):
        return self.velocita


veicolo = Veicolo("Opel", "Mokka", 2017)
print(veicolo.__str__())
for i in range(10):
    veicolo.accellerare()
print(veicolo.get_speed())
for i in range(10):
    veicolo.frenare()
print(veicolo.__str__())

