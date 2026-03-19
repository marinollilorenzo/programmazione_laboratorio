b = True
while b:
    try:
        inpt = int(input("Inserisci un valore intero:"))
        b = False
        print(inpt**2)
    except ValueError:
        print("Errore: devi inserire un intero!")