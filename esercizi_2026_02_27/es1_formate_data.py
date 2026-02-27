def formate_data_from_minute(minute):
    MINUTE_FORMAT = 60
    return minute//MINUTE_FORMAT, minute%MINUTE_FORMAT

def formate_data(minute):
    ora, minuti = formate_data_from_minute(minute)
    return f"{ora}h:{minuti}min"


def main():
    print("Esercizi del 27-02-2026")
    
    print("Formatta minuti in ore:")
    print(formate_data(int(input("Inserisci il numero di minuti da formattare:"))))
    

if __name__ == "__main__":
    main()
