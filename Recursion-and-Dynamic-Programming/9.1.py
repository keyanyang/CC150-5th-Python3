def stair(n):
    if n == 0:
        return 1
    if n < 0 :
        return 0
    else:
        return stair(n-1) + stair(n-2) + stair(n-3)

n = 6
print ('If staircase has {} steps, there would be {} possible ways.'.format(n, stair(n)))
