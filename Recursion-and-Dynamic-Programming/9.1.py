def stair(n, counter = [0]):         #counter = [0] here will not affect the increase of counter in the recursion
    if n == 0:
        counter[0] += 1
    if n < 0 :
        return 
    else:
        stair(n-1, counter)
        stair(n-2, counter)
        stair(n-3, counter)
    return counter[0]

n = 4
print ('If staircase has {} steps, there would be {} possible ways.'.format(n, stair(n)))
