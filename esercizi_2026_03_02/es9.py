def count_word(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
        d = {}
        for line in lines:
            for word in line.strip("\n").split(","):
                if word in d.keys():
                    d[word] += 1
                else:
                    d[word] = 1
    return d

print(count_word("DOCS/word.csv"))