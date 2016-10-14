def findMagic(array):
    return findMagicRe(array, 0, len(array))

def findMagicRe(array, start, end):
    mid = (start + end)//2
    if array[mid] == mid:
        return mid
    if array[mid] < mid:
        return findMagicRe(array, mid, end)
    else:
        return findMagicRe(array, start, mid)
    

print (findMagic([-40,-30,-10,-5,0,1,2,6,8]))
print (findMagic([-10,1,8,10,50,100]))
    
