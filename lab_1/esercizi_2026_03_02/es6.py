def count_number(l):
    d = {}
    for item in l:
        item2 = item.lower()
        if item2 in d.keys():
            d[item2] += 1
        else:
            d[item2] = 1
    return d

l = count_number(l=["uno", "due", "tre", "quattro", "cinque", "uno", "due", "uno"])
print(l)