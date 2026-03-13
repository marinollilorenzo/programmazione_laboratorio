class Poligono:
    
    def __init__(self, n_lati):
        self.n_lati = n_lati
    
    def __str__(self):
        return f"Sono un poligono con {self.n_lati} lati"
    
class Quadrilatero(Poligono):

    def __init__(self):
        super().__init__(4)
        
    def __str__(self):
        return f"Sono un quadrilatero con {self.n_lati} lati"

class Rettangolo(Quadrilatero):
    
    def __init__(self, base, altezza):
        super().__init__(self)
        self.base = base
        self.altezza = altezza
    
    def __str__(self):
        return f"Sono un rettangolo con altezza:{self.altezza} e base:{self.base}"
    
    def get_perimetro(self):
        return 2 * (self.base + self.altezza)
    
    def get_area(self):
        return self.base * self.altezza

class Triangolo(Poligono):
    
    def __init__(self, l1, l2, l3):
        super().__init__(3)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    def __str__(self):
        return f"Sono un triangolo e i miei lati sono lunghi: \nl1:{self.l1}\nl2:{self.l2}\nl3:{self.l3}"
    
    def get_perimetro(self):
        return self.l1 + self.l2 + self.l3
    
    def is_equilatero(self):
        return True if self.l1 == self.l2 and self.l2 == self.l3 else False