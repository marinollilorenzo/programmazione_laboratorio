def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

def main():
    print("Esercizi del 27-02-2026")
    
    print("Numero primo:")
    number = int(input("Inserisci un numero da verificare se è primo:"))    
    print(f"il numero '{number}' " + ("è" if is_prime(number) else "non è") + " primo")

if __name__ == "__main__":
    main()
