def rotate():
    x = [ ['p00', 'p01', 'p02', 'p03'],
          ['p10', 'p11', 'p12', 'p13'],
          ['p20', 'p21', 'p22', 'p23'],
          ['p30', 'p31', 'p32', 'p33'] ]
    for i in zip(*x):
        print (list(reversed(i)))
        
    
if __name__ == "__main__":
    print ("# 1.5")
    rotate()
