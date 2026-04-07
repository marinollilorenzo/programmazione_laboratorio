class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name:str):
        self.name = name
        
    def get_data(self, city:str)->list:
        try:
            with open(self.name, "r")as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise ExamException("Errore: file non trovato!")
        ret = []
        for line in lines:
            l = line.strip().split(",")
            if len(l) == 3 and l[2].lower() == city.strip().lower():
                try:
                    l[1] = float(l[1])
                    ret.append([l[0], l[1]])
                except ValueError:
                    print("Errore: tipo non convertibile in float")
        if len(ret) == 0:
            raise ExamException("Errore: il nome della città non è presente nel file")
        return ret

def compute_slope(time_series: list, first_year: int, last_year: int)-> float:
    if last_year - first_year <= 0:
        raise ExamException("Errore: intervallo di anni non valido")
    dct_years = {}
    for line in time_series:
        year = int(line[0].split("-")[0])
        if year in range(first_year, last_year + 1):
            if year not in dct_years:
                dct_years[year] = {
                    "sum" : 0,
                    "len" : 0
                }
            dct_years[year]["sum"] += line[1]
            dct_years[year]["len"] += 1
    if len(dct_years) == 0:
        raise ExamException("Errore: intervallo di anni non valido")
    dct_years_mean = {year : round(dct_years[year]["sum"] / dct_years[year]["len"], 3) for year in dct_years if dct_years[year]["len"] >= 6}
    if len(dct_years_mean) == 0:
        raise ExamException("Errore: denominatore uguale a 0")
    x_segnato = sum(dct_years_mean) / len(dct_years_mean)
    y_segnato = sum(dct_years_mean[year] for year in dct_years_mean) / len(dct_years_mean)
    
    m_den = sum((year - x_segnato)**2 for year in dct_years_mean) 
    if m_den == 0:
        raise ExamException("Errore: il denominatore del coefficiente angolare è uguale a 0")
    
    m = sum((year - x_segnato) * (dct_years_mean[year] - y_segnato) for year in dct_years_mean) / m_den
    
    return m

    
time_series_file = CSVTimeSeriesFile(name="GlobalLandTemperaturesByMajorCity.csv")
time_series_rome = time_series_file.get_data(city="Rome")

m = compute_slope(time_series_rome, 2010, 2013)

# for item in time_series_rome:
#     print(item)

# print(len(time_series_rome))

print(m)