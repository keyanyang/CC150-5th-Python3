class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):     #step1
        self.head = None
        self.tail = None
    
    def addNode(self, inse):        #step2
        nde = Node(inse)       #node including .value and .next
        if self.head == None:
            self.head = nde
            self.tail = nde
        else:
            self.tail.next = nde
            self.tail = nde
    
    def __str__(self):
        nodestore = [str(self.head.value)]
        index = self.head
        while index.next != None:
            index = index.next
            nodestore.append(str(index.value))
        return "->".join(nodestore)

def randomLinkedList(leng, min, max):
    from random import randint
    rll = LinkedList()
    for i in range(leng):
        value = randint(min, max)
        rll.addNode(value)
    return rll

def kth(ll, k):
    if k <= 0:
        return "k must be larger than 0"
    rightside = ll.head
    for i in range(k-1):
        if rightside.next != None:
            rightside = rightside.next
        else:
            return "k is too large"
    leftside = ll.head      #at this time pointer2 is tail
    while rightside.next != None:
        rightside = rightside.next
        leftside = leftside.next        #this would be just like a stick with leftside and rightside. Both sides move together and when rightside reaches the territory, leftside is the result
    return 'The {}th to last element is {}'.format(k, leftside)        
                
test = randomLinkedList(5, 1, 50)
print (test)
print(kth(test,2))

