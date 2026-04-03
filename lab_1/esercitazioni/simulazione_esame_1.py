class ExamException:
    pass
class CSVTimeSeriesFile:
 
    def __init__(self, name:str):
        try:
            with open(name, "r") as f:
                self.name = name
        except FileNotFoundError:
            raise ExamException("Errore: file indicato non esistente")
        except:
            raise ExamException("Errore: file non leggibile")
        
    def get_data(self)-> list:
        with open(self.name, "r") as f:
           lines = f.readlines()
        lst = []
        for line in lines:
            try:
                l = line.strip("\n").split(",")
                val = float(l[1])
                if val >= 0:
                    l[1] = round(val, 3)
                    lst.append(l)
                else:
                    print(f"Errore: valore {val} negativo")
            except ValueError:
                print(f"Errore nel parsing della riga {line}")
        return lst


def compute_variations(time_series: CSVTimeSeriesFile, first_year: int, last_year: int, N: int)->dict:
    if N >= last_year-first_year:
        raise ExamException("Errore: N deve essere minore della finestra di intervallo")
    data = time_series.get_data()
    dct_years = {}
    dct_years_len = {}
    #Inizializzo dizionari
    for i in range(first_year, last_year + 1):
        dct_years[i] = 0
        dct_years_len[i] = 0
    #scorro il file csv per trovare tutti gli anni presenti e somamre i valori delle medie del mese tenendo conto di tutti i mesi per eventuali mesi mancanti
    for line in data:
        year = int(line[0].strip().split("/")[0])  
        if year in dct_years:
            dct_years[year] += line[1]
            dct_years_len[year] += 1
    dct_years_mean = {} 
    #per ogni anno trovo la media annuale
    for i in range(first_year, last_year + 1):
        if dct_years_len[i] > 0:
            dct_years_mean[i] = round(dct_years[i] / dct_years_len[i], 3)
        else:
            dct_years_mean[i] = 0
    dct_years_mean_last_n = {}
    
    for year in range(first_year + N, last_year + 1):
        dct_years_mean_last_n[year] = 0
        for i in range(i - N, i):
            dct_years_mean_last_n[year] += dct_years_mean[i] 
        dct_years_mean_last_n[year] /= N
        dct_years_mean_last_n[year] = round(dct_years_mean_last_n[year],3)
    dct_years_mean_diff = {}
    for year in range(first_year + N, last_year + 1):
        dct_years_mean_diff[year] = round(dct_years_mean[year] - dct_years_mean_last_n[year], 3)

    return dct_years_mean_diff

def get_years_out_of_range(time_series: CSVTimeSeriesFile, start_temp: float, end_temp: float)->dict:
    if end_temp < start_temp:
        raise ExamException("Errore: temperatura finale minore di temperatura iniziale")
    lst_years = []
    data = time_series.get_data()
    for line in data:
        if not start_temp <= line[1] <= end_temp:
            year = int(line[0].strip().split("/")[0])
            if year not in lst_years:
                lst_years.append(year)
    return lst_years
            
            
                
#time_series_file = CSVTimeSeriesFile(name="lab_1/esercitazioni/GlobalTemperatures.csv")
time_series_file = CSVTimeSeriesFile(name="GlobalTemperatures.csv")

print(compute_variations(time_series_file, 1900, 1904, 3))
print(get_years_out_of_range(time_series_file, 0, 15))