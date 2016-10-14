def subSet(set):
    current = [[]]
    for s in set:
        temp = []
        for i in current:
            temp.append(i + [s])
            temp.append(i + [])
        current = temp
    return current

S = set([1, 2, 3, 4])
print (subSet(S))
