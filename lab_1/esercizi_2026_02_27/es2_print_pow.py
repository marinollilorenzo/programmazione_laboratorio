def pow(x, n = 2):
    return x ** n

def main():
    print("Esercizi del 27-02-2026")
    
    print("Elevamento a potenza:")
    x = int(input("Inserisci il numero da elevare al quadrato e al cubo:"))
    print(f"Il numero {x} elevato al quadrato è {pow(x)}\nIl numero {x} elevato al cubo è {pow(x,3)}")

if __name__ == "__main__":
    main()
