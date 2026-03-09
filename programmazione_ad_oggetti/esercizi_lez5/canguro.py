class Canguro:
    
    def __init__(self, contenuto_tasca = None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca
    
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)
    
    def __str__(self):
        return f"Contenuto  tasca: {self.contenuto_tasca}"
    
can = Canguro()
guro = Canguro()
can.intasca("pippo")
can.intasca("cocaina")

print(can)
print(guro)