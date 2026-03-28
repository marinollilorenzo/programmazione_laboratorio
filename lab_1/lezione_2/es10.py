def remove_duplicate(filepath):
    new_file = open("DOCS/nuovo.txt", "w")
    copia = []
    with open(filepath, "r") as f:
        for line in f.readlines():
            if line not in copia:
                copia.append(line)
        for line in copia:
            new_file.write(line)
    new_file.close()

remove_duplicate("DOCS/duplicated.txt")
