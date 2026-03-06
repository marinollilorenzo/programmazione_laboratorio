def sum_list(lista : list):
    sum = 0
    for item in lista:
        sum += int(item)
    return sum


lista = [1,2,3,4]
print(sum_list(lista))