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

def partition(ll, x):
    p1 = ll.head
    p2 = ll.head.next
    while p2 != None:
        if p2.value >= x:
            p1 = p1.next
            p2 = p2.next
        else:
            p1.next = p2.next
            p2.next = ll.head
            ll.head = p2
            p2 = p1.next
            
                
test = randomLinkedList(5, 1, 100)
print (test)
partition(test, 35)
print (test)
