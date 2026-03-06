def itemList(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False


print(itemList(l1=[1,2,3,4,5], l2=[2,10,20,30,40]))