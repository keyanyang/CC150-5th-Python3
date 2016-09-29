def isper(string1, string2):
    a = string1
    b = string2
    hash_a = {}
    hash_b = {}
    for i in range(0,len(a)):
        if a[i] not in hash_a:
            hash_a[a[i]] = 0
        else: 
            hash_a[a[i]] += 1
    for i in range(0,len(b)):
        if b[i] not in hash_b:
            hash_b[b[i]] = 0
        else: 
            hash_b[b[i]] += 1
    if hash_a == hash_b:
        return True
    else:
        return False

if __name__ == "__main__":
    print ("# 1.3")
    print(isper('abdcd','cddab'))
