def contains(word, letter):
    i = 0
    for char in word:
        if letter == char:
            i += 1
    return i

def main():
    print("Esercizi del 27-02-2026")
    
    print("Lettere contenute dentro una parola:")
    word = input("Inserisci un parola:")
    letter = input("Inserisci una lettera:")
    
    print(f"la lettera '{letter}' è presente {contains(word, letter)} volte dentro la parola '{word}'")

if __name__ == "__main__":
    main()
