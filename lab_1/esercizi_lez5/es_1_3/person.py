class Person:
    def __init__(self, role, name, surname):
        self.ruolo = role
        self.nome = name
        self.cognome = surname
    
    def saluta(self):
        return f"Hi, I'm {self.ruolo}, {self.nome} {self.cognome}"