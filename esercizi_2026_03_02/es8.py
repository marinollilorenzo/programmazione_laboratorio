def count_word(filepath, word_search):
    with open(filepath, "r") as f:
        lines = f.readlines()
        c = 0
        for line in lines:
            for word in line.split(","):
                if word_search == word:
                    c += 1
    return c

print(count_word("DOCS/word.csv", "ciao"))