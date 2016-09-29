x = [ ['p00', 'p01', 'p02', 'p03'],
      ['p10', 'p11', 'p12', 'p13'],
      ['p20', 'p21', 'p22', 'p23'],
      ['p30', 'p31', 'p32', 'p33'] ]
def original():
    for i in range(0,len(x)):
        print (x[i])
            
def rotateleft():    
    for i in zip(*x):
        print (list(reversed(i)))

def rotateright():    
    uzx = list(zip(*x))    
    for i in range(0,len(uzx)):
        print (list(uzx[-(i+1)]))
            
if __name__ == "__main__":
    print ("# 1.5")
    print ('original image:')
    original()
    print ('rotate the image by 90 degree left:')
    rotateleft()
    print ('rotate the image by 90 degree right:')
    rotateright()
