def main():
    print("Esercizi del 27-02-2026")
    
    print("Summa n numbers:")
    t = 1
    sum = 0
    while t != 0:
        t = int(input("Inserisci un numero da sommare agli altri./n[0] per uscire:"))
        sum += t
    print(f"la somma di tutti i valori che hai inserito è {sum} ")

if __name__ == "__main__":
    main()
