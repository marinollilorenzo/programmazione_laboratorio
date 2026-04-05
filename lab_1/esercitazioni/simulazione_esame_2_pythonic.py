class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    
    def __init__(self, name):
        try:
            self.name = name
            with open(name, "r") as f:
                l = f.readline()
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire il file")
        except:
            raise ExamException("Errore: il file è vuoto o non contiene dati validi")
        if len(l) == 0:
                raise ExamException("Errore: il file è vuoto")
    
    def _parse_line(self, line: str, country: str)->list:
        try:
            l = line.strip().split(",")
            if(len(l) == 3): 
                return ([l[0], round(float(l[1]), 3)]) if l[2].lower().startswith(country.strip().lower()) else None
        except ValueError:
            pass
                #print(f"Errore nel parsing della riga {line}")
        
    def get_data(self, country: str)-> list:
        with open(self.name, "r") as f:
            lines = f.readlines()
        ret = [self._parse_line(line, country) for line in lines if self._parse_line(line, country) is not None]
        if len(ret) == 0:
            raise ExamException("Errore: il nome del paese non è presente nel file")
        return ret
                
def compute_variations(time_series_1: list, time_series_2: list, first_year: int, last_year: int)-> dict:
    if not isinstance(first_year, int) or not isinstance(last_year, int):
        raise ExamException("Errore: l'anno inserito non è un intero")
    dct_counting = {}
    for line in time_series_1:
        year_country = int(line[0].split("-")[0])
        if year_country in range(first_year, last_year + 1):
            if year_country not in dct_counting:
                dct_counting[year_country] = {"sum" : 0, "len" : 0}
            dct_counting[year_country]["len"] += 1
            dct_counting[year_country]["sum"] += line[1]
    dct_country_1 = {str(year) : round(dct_counting[year]["sum"] / dct_counting[year]["len"], 3) for year in range(first_year, last_year + 1) if year in dct_counting and dct_counting[year]["len"] > 0}
        
    dct_counting = {}
    for line in time_series_2:
        year_country = int(line[0].split("-")[0])
        if year_country in range(first_year, last_year + 1):
            if year_country not in dct_counting:
                dct_counting[year_country] = {"sum" : 0, "len" : 0}
            dct_counting[year_country]["len"] += 1
            dct_counting[year_country]["sum"] += line[1]
    dct_country_2 = {str(year) : round(dct_counting[year]["sum"] / dct_counting[year]["len"], 3) for year in range(first_year, last_year + 1) if year in dct_counting and dct_counting[year]["len"] > 0}
        
    dct_diff = {str(year) : round(dct_country_2[str(year)] - dct_country_1[str(year)], 3) for year in range(first_year, last_year + 1) if str(year) in dct_country_1 and str(year) in dct_country_2}

    if len(dct_diff) == 0:
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")
    return dct_diff
            
time_series_file = CSVTimeSeriesFile("GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(country="Italy")
time_series_france = time_series_file.get_data(country="France")
dct = compute_variations(time_series_italy, time_series_france, 1900, 1902)
print(dct)

#-----------TEST------------------


time_series_test_1 = [
    ["2024-01-01", 12.5],
    ["2024-02-01", 13.5],
    ["2024-03-01", 11.5],
    ["2024-04-01", 12.5],
    ["2024-05-01", 13.5],
    ["2024-06-01", 11.5],
    ["2024-07-01", 12.5],
    ["2024-08-01", 13.5],
    ["2024-09-01", 11.5],
    ["2024-10-01", 12.5],
    ["2024-11-01", 13.5],
    ["2024-12-01", 11.5],
    ["2025-01-01", 20],
    ["2025-02-01", 22],
    ["2025-03-01", 18],
    ["2025-04-01", 20],
    ["2025-05-01", 22],
    ["2025-06-01", 18],
    ["2025-07-01", 20],
    ["2025-08-01", 22],
    ["2025-09-01", 18],
    ["2025-10-01", 20],
    ["2025-11-01", 22],
    ["2025-12-01", 18],
]

time_series_test_2 = [
    ["2024-01-01", 12.5],
    ["2024-02-01", 13.5],
    ["2024-03-01", 11.5],
    ["2024-04-01", 12.5],
    ["2024-05-01", 13.5],
    ["2024-06-01", 11.5],
    ["2024-07-01", 12.5],
    ["2024-08-01", 13.5],
    ["2024-09-01", 11.5],
    ["2024-10-01", 12.5],
    ["2024-11-01", 13.5],
    ["2024-12-01", 11.5],
    ["2025-01-01", 30],
    ["2025-02-01", 32],
    ["2025-03-01", 28],
    ["2025-04-01", 30],
    ["2025-05-01", 32],
    ["2025-06-01", 28],
    ["2025-07-01", 30],
    ["2025-08-01", 32],
    ["2025-09-01", 28],
    ["2025-10-01", 30],
    ["2025-11-01", 32],
    ["2025-12-01", 28],
]

dct = compute_variations(time_series_test_1, time_series_test_2, 2020, 2025)

risultato_atteso_test = {
    "2024" : 0,
    "2025" : 10
}
for year in risultato_atteso_test:
    if risultato_atteso_test[year] != dct[year]:
        print("test fallito")
        exit(1)
print("test superato")
