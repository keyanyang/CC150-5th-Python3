def replace(str):
    input = list(str)
    for i in range(0,len(input)):
        if input[i] == ' ':
            input[i] = '%20'
        print(input[i], end ='')
            
    
if __name__ == "__main__":
    print ("# 1.4")
    replace('You Know Nothing John Snow')
