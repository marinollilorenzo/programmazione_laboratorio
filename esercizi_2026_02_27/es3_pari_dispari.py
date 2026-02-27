def is_pari(x):
    return x % 2 == 0

def main():
    print("Esercizi del 27-02-2026")
    
    print("Numero pari o dispari:")
    x = int(input("Inserisci il numero da verificare se è pari o dispari:"))
    print("Il numero è pari" if is_pari(x) else "Il numero è dispari")
        
if __name__ == "__main__":
    main()
