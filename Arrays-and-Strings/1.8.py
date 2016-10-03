def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    elif str1 == str2:
        return False
    else:
        str3 = str2 + str2
        return str1 in str3        
           
if __name__ == "__main__":
    print ("# 1.8")
    print (isRotation("waterbottle", "erbottlewat"))
    
