while True:
    try:
        inpt = int(input(f"""
    Menù:
    [1] Calcolare la somma di due numeri.
    [2] Calcolare la differenza tra due numeri.
    [0] Uscire. 
    Inserisci il valore:"""))
        match inpt:
            case 0:
                print("Good Bye")
                break
            case 1:
                while True:
                    try:
                        x, y = input("dammi due numeri separati dalla virgola:").strip().split(",")
                        x, y = int(x), int(y)
                        break
                    except ValueError:
                        print("Errore: devi inserire due interi separati dalla virgola(es 5,4)!")
                print(f"La somma è {x+y}")
            case 2:
                while True:
                    try:
                        x, y = input("dammi due numeri separati dalla virgola:").strip().split(",")
                        x, y = int(x), int(y)
                        break
                    except ValueError:
                        print("Errore: devi inserire due interi separati dalla virgola(es 5,4)!")
                print(f"La differenza è {x-y}")
            
            case _:
                print("valore non valido")
    except ValueError:
        print("Errore: devi inserire un intero!")