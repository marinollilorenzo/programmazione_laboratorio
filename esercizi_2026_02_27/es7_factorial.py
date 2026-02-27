def fatt(number):
    fatt = 1
    for i in range(2, number + 1):
        fatt *= i
    return fatt

def main():
    print("Esercizi del 27-02-2026")
    
    print(" --- Fattoriale --- ")
    number = int(input("Inserisci un numero da calcolare il fattoriale:"))
    
    print(f"il numero '{number}' fattoria è pari a {fatt(number)}")

if __name__ == "__main__":
    main()
