class ExamException(Exception):
    pass

class EarthquakeFile:
    
    def __init__(self, name:str):
        try:
            with open(name, "r") as f:
                f.readline()
            self.name = name
        except Exception:
            raise ExamException("Errore: impossibile accedere al registro sismico")
        
    def get_data(self, min_magnitudo: float)->list:
        lst_ret = []
        with open(self.name) as f:
            next(f)
            for line in f:
                try:
                    data, regione, magnitudo, profondita = line.strip().split(",")
                    magnitudo = float(magnitudo)
                    profondita = float(profondita)
                    if profondita < 50:
                        if magnitudo >= min_magnitudo: 
                            lst_ret.append([data, regione, magnitudo])    
                    else:
                        print(f"Sisma del {data} ignorato: troppo profondo")
                except ValueError:
                    pass
        return lst_ret
    
def count_earthquakes_by_year(data_list: list, target_regione: str)->dict:
    if not isinstance(target_regione, str):
        raise ExamException("Errore: la regione deve essere una stringa")
    dct = {}
    for item in data_list:
        if item[1] == target_regione:
            year = int(item[0].strip().split("-")[0])
            dct[year] = dct.get(year, 0) + 1
    if(len(dct) == 0):
        raise ExamException("Nessun dato sismico per la regione richiesta")
    return dct
    

earthquake = EarthquakeFile("data/earthquakes.csv")
data = earthquake.get_data(1)

for item in data:
    print(item)
dct = count_earthquakes_by_year(data, "Lazio")

print(dct)