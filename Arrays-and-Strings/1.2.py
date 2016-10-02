def reverse(string):
    a = string
    print(a[::-1])

def reverse2(string):
    a = string
    for i in range(0,len(a)):
        print(a[-(i+1)], end = '')

if __name__ == "__main__":
    print ("# 1.2")
    reverse('pen apple')
    reverse2('pen apple')
