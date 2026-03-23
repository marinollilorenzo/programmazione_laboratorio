def triangle(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        return None
    if x == y and y == z and x == z:
        return "equilatero"
    if x == y or x == z or y == z:
        return "isoscele"
    return "scaleno"

def main():
    print("Esercizi del 27-02-2026")
    
    print("Da 3 numeri un triangolo:")
    l = input().split(",")
    x, y, z = [int(i) for i in l]
    
    res = triangle(x,y,z)
    print("Il triangolo non può essere fatto" if res == None else f"Il triangolo è {res}")

if __name__ == "__main__":
    main()
