class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    
    def __init__(self, name: str):
        try:
            with open(name, "r") as f:
                f.readline()
            self.name = name
        except FileNotFoundError:
            raise ExamException("Errore: file non trovato")
        except:
            raise ExamException("Errore: impossibile aprire il file o file vuoto")

    def get_data(self)-> list:
        ret = []
        with open(self.name, "r") as f:
            for line in f:
                l = line.strip().split(",")
                if len(l) == 3:
                    try:
                        date = l[0]
                        value = float(l[1])
                        if float(l[2]) < 5:
                            ret.append([date, round(value, 3)])
                        else:
                            print("Data saltata perchè valore troppo incerto")
                    except ValueError:
                        pass
                        #print(f"Errore nel parsing a float della riga:`{line}`")
        return ret
        
def compute_month_variation(time_series: list, first_year: int, second_year: int)->dict:
    if not isinstance(first_year, int) or not isinstance(second_year, int):
        raise ExamException("Errore: gli anni inseriti devono essere di tipo intero.")
    if second_year <= first_year:
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo.")
    dct = {
        first_year:{},
        second_year:{}
    }
    for item in time_series:
        date = item[0].strip().split("-")
        value = item[1]
        year, month = int(date[0]), int(date[1])
        if year == first_year or year == second_year:
            dct[year][month] = value
    dct_ret = {}
    for i in range(1, 13):
        if i in dct[first_year] and i in dct[second_year]:
            dct_ret[i] = round(dct[second_year][i] - dct[first_year][i], 3)
        else:
            print(f"La variazione per il mese {i} non può essere calcolata")
    if dct_ret == {}:
        raise ExamException("Gli anni considerati non hanno mesi validi")
    return dct_ret



time_series_file = CSVTimeSeriesFile(name="data/Temperatures.csv")
data = time_series_file.get_data()
dct = compute_month_variation(data, 1900, 2000)

print(dct)