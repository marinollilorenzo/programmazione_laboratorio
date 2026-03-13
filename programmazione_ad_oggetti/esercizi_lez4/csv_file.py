class CSVFile:
    
    def __init__(self, filepath):
        if(isinstance(filepath, str)):
            self.filepath = filepath
        else:
            raise Exception("filepath non è una stringa!")
        try:
            with open (self.filepath, 'r') as fi:
                fi.readline()
        except FileNotFoundError:
            print("File non trovato o non esistente, assicurati che il file sia presente:")
        except Exception as e:
            print(f"Errore inateso:{e}")

    def get_data(self, start=None, end=None):
        start = 0 if start is None or start <= 0 or (end is not None and start > end) else start
        lst = []
        try:
            with open (self.filepath, 'r') as fi:
                lines = fi.readlines()
                end = len(lines) if end is None or end <= 0 or end < start or end >= len(lines) else end + 1
                for i in range(start, end):
                    lst.append(lines[i].strip("\n").split(","))
        except FileNotFoundError:
            print("File non trovato o non esistente, assicurati che il file sia presente")
        except Exception as e:
            print(f"Errore inateso: {e}")
        return lst

class NumericalCSVFile(CSVFile):
    def __init__(self, filepath):
        super().__init__(filepath)
    
    def _safe_float(self, value):
        try:
            return float(value)
        except ValueError:
            print(f"Errore nel parsing della stringa:'{value}' in float")
            return value
    
    def convert_all_in_float(self):
        lst = super().get_data()
        for line in lst[1:]:
            line[1:] = [self._safe_float(number) for number in line[1:]]
        return lst
        
        

csv_file = CSVFile("DOCS/shampo.csv")
lst = csv_file.get_data(start=10, end=4)
for i, item in enumerate(lst):
    print(i, item)

