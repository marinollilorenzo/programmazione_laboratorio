while True:
    try:
        inpt = int(input("Inserisci un valore intero:"))
        break
    except ValueError:
        print("Errore: devi inserire un intero!")
        
print(inpt**2)