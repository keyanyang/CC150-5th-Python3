x = [ [1, 2, 3],
      [4, 5, 6],
      [7, 0, 9],
      [10, 11, 12] ]
         
def setZero(): 
    row = {}
    col = {} 
    for i in range(0, len(x)):
        row[i] = False 
    for j in range(0, len(x[0])):
        col[j] = False  
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            if x[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            if row[i] == True or col[j] == True:
                x[i][j] = 0
    print (x)
            
if __name__ == "__main__":
    print ("# 1.7")
    setZero()
