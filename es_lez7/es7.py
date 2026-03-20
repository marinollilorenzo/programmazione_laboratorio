def get_two_numbers()->tuple[int, int]:
    while True:
        try:
            x, y = input("dammi due numeri separati dalla virgola:").strip().split(",")
            x, y = int(x), int(y)
            return x,y
        except ValueError:
            print("Errore: devi inserire due interi separati dalla virgola(es 5,4)!")
    

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
                x, y = get_two_numbers()
                print(f"La somma è {x+y}")
            case 2:
                x, y = get_two_numbers()
                print(f"La differenza è {x-y}")
            
            case _:
                print("valore non valido")
    except ValueError:
        print("Errore: devi inserire un intero!")