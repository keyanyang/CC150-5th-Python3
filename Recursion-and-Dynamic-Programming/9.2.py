def path(x,y):      #in this problem, x would be larger than 0 and y would be less than 0
    if x == 0 and y == 0:
        return 1
    if x< 0 or y > 0:
        return 0
    else:
        return path(x-1, y) + path(x, y+1)

def showpath(x, y, list = []):
    list = list + [(x,y)]
    if x == 0 and y == 0:
        print (list)
        return
    if x < 0 or y > 0:
        return
    else:
        showpath(x - 1, y, list)
        showpath(x, y + 1, list)

    
x, y = 2, -2
print(path(x,y))
showpath(x,y)
