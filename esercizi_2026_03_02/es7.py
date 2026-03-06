def sumSales(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()[1:]
        s = 0
        for line in lines:
            s += float(line.split(",")[1])
    return s

print(sumSales("DOCS/shampo.csv"))