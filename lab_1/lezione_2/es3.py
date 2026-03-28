def changeList(l, i, j):
    l[i], l[j] = l[j], l[i]

l = [1,2,3,4,5]

changeList(l, 0, 4)

for item in l:
    print(item)
    