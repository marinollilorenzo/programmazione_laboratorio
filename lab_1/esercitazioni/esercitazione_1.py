class ExamException(Exception):
    pass

class MovingAverage:
    
    def __init__(self, length:int):
        if not isinstance(length, int) or length <= 0:
            raise ExamException("Errore: lunghezza deve essere un intero > 0")
        self.length = length
        
    def compute(self, lst:list)-> list:
        if not isinstance(lst, list):
            raise ExamException("Errore: L'argomento passato non è una lista")
        if len(lst) == 0:
            raise ExamException("Errore: La lista passata è vuota")
        if len(lst) < self.length:
            raise ExamException("Errore: La lista non può essere minore della lunghezza della finestra")
        if len(lst) % self.length != 0:
            raise ExamException("Errore: lunghezza finestra non compatibile con la lunghezza della lista")
        for item in lst:
            if not isinstance(item, float) and not isinstance(item, int):
                raise ExamException("Errore: la lista deve contenere solamente numeri")
        
        ret = [(sum(lst[i : i+self.length]) / self.length) for i in range(len(lst) - self.length + 1)]
         
        # for i in range(len(lst)-self.length+1):
        #     s = 0
        #     for j in range(self.length):
        #         s += lst[i+j]
        #     ret.append(s/self.length)
        
        return ret
    

mov = MovingAverage(2)
print(mov.compute([2, 4, 8, 16]))