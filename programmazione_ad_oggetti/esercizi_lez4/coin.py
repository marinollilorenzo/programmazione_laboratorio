class Coin:
    def __init__(self, face="T"):
        self.face = face
    
    def lancio_coin(self):
        from random import randint
        rand = randint(0,1)
        self.face = "T" if rand == 0 else "C"
    
    def get_face(self):
        return self.face
    
coin = Coin()
print(coin.get_face())
l = []
for i in range(10):
    coin.lancio_coin()
    l.append(coin.get_face())
print(l)