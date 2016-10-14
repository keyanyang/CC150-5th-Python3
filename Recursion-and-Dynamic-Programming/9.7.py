def fillup(x, y, color, area):
    if x < 0 or y < 0 or x >= len(area) or y >= len(area[0]):
        return
    elif area[x][y] == 0:
        area[x][y] = color
        fillup(x - 1, y, color, area)
        fillup(x + 1, y, color, area)
        fillup(x, y - 1, color, area)
        fillup(x, y + 1, color, area)
    return area
        
a = [[0 for i in range(4)] for j in range(5)]
print('orignial area:')
print(a)
x = 1
y = 2
blue = '#0000ff'
print('blue area:')
print(fillup(1, 2, blue, a))
