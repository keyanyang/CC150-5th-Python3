x = [ [1, 2, 3],
      [4, 5, 6],
      [7, 0, 9],
      [10, 11, 12] ]

          
def setZerousingnp():  #method2--use numpy
    import numpy as np  
    flag = 0   
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            if x[i][j] == 0:
                flag += 1
    if flag >= 1:
        zerom = np.zeros((len(x), len(x[0])))
    else: 
        zerom = x
    print (zerom)
            
if __name__ == "__main__":
    print ("# 1.7")
    setZerousingnp()
