from datetime import datetime

DAYS = {1:31, 2:28, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31
}   

def is_bisestile(year:int)->bool:
    """
    Ritorna
        True se l'anno è bisestile
        False altrimenti
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_from_year_and_month(year:int, month: int)-> int:
    """
    Da il mese e l'anno ritorniamo il numero di giorni
    """
    if month == 2 and is_bisestile(year=year):
        return 29
    else:
        return DAYS[month]
    
def getAgeFromDate(date_now:datetime, day:int, month:int, year:int):
    if month > date_now.month or (month == date_now.month and day > date_now.day):
        return date_now.year - year - 1
    else:
        return date_now.year - year

def lastToBirthday(date_now:datetime, day:int, month:int, year:int):
    giorni = 0
    if date_now.month == month and date_now.day < day:
        giorni += day - date_now.day - 1
    else:
        giorni += days_from_year_and_month(date_now.year, date_now.month) - date_now.day
        year_end = date_now.year + (1 if date_now.month >= month else 0)
        for i in range(date_now.month+1, month + (12 if year_end != date_now.year else 0)):
            giorni += days_from_year_and_month(year=(date_now.year if i <= 12 else year_end), month=(i if i <= 12 else i%12))
        giorni += day -1
        
    secondi = 60 - date_now.second if date_now.second > 0 else 0
    minuti = 60 - date_now.minute - (1 if secondi > 0 else 0)
    if minuti == 60:
        minuti = 0
    ore = 24 - date_now.hour - (1 if minuti > 0 or secondi > 0 else 0)
    if ore == 24:
        ore = 0
    
    return giorni, ore, minuti, secondi

date = input("Inserisci la data di nascita per scoprire quanti giorni mancano al tuo compleanno (formato obbligatorio: DD/MM/AAAA):")
date_now = datetime.now()
date = date.strip()
if not "/" in date:
    raise Exception("La data non contiene il formato corretto")
if len(date.split("/")) != 3:
    raise Exception("La data non contiene il formato corretto")
try:
    day, month, year = date.split("/")
    day, month, year = int(day), int(month), int(year)
except ValueError:
    raise Exception("Devi inserire numeri nella data!")
if year >= date_now.year or year < 1000 or month <= 0 or month > 12 or day <= 0 or day > days_from_year_and_month(year=year, month=month):
    raise Exception("Errore nella scrittura della data")

giorni, ore, minuti, secondi = lastToBirthday(date_now=date_now, day=day, month=month, year=year)

print(f"rimangono {giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi ai tuoi {getAgeFromDate(date_now=date_now, day=day, month=month, year=year) + 1} anni")