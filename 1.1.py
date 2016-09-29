def unique(string):
    a = string
    b = {}
    for i in range(0, len(a)):
        if a[i] not in b:
            b[a[i]] = 1
        else:
            b[a[i]] += 1
    for k, v in dict.items(b):
        if v >= 2:
            print(k, v)   #so this will show the key which is not unique and the number of it

if __name__ == "__main__":
    print ("# 1.1")
    unique('ayaxbbcyc')
