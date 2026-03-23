def italian_number(l):
    d = {
        1 : "uno", 2 : "due", 3 : "tre", 4 : "quattro",
        5 : "cinque", 6 : "sei", 7 : "sette", 8 : "otto",
        9 : "nove", 0: "zero"}
    lret = []
    for item in l:
        lret.append(d[item])
    return lret

l = italian_number(l=[1,0,8,4,5])
for item in l:
    print(item)