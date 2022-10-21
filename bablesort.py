def bable(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i ):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l
print(bable([5,6,78,2,32,7,9,63,4,0]))
