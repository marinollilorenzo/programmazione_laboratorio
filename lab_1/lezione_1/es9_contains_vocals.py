def contains_vocals(word, limit = ["a", "e", "i", "o", "u"]):
    i = 0
    for letter in word:
        for lim in limit:
            if letter == lim:
                i += 1
    return i
    
def main():
    print("Esercizi del 27-02-2026")
    
    print("vocali contenute dentro una parola:")
    word = input("Inserisci un parola:")
    
    print(f"le vocali sono presenti {contains_vocals(word)} volte dentro la parola '{word}'")

if __name__ == "__main__":
    main()
