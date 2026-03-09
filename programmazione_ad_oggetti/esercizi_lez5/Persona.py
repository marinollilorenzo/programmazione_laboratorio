class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        return f"Ciao sono {self.ruolo}, {self.nome} {self.cognome}"

class Studente(Persona):

    def __init__(self, nome, cogmome, corso = None):
        super().__init__("Studente UNITS", nome, cogmome)
        if corso is None:
            self.corso = []
        else:
            self.corso = corso
    
    def saluta(self):
        return super().saluta() + f""" > frequento i corsi {self.corso}"""

class Docente(Persona):

    def __init__(self, nome, cogmome, corso = None):
        super().__init__("Docente UNITS", nome, cogmome)
        if corso is None:
            self.corso = []
        else:
            self.corso = corso
    
    def saluta(self):
        return super().saluta() + f""" > Docente dei corsi {self.corso}"""
    

irene = Studente("Irene", "Rossi", ["Programmazione", "Analisi 2", "Sistemi Operativi"])
print(irene.saluta())