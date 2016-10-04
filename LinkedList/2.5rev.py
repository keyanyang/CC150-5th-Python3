class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):   
        self.head = None
        self.tail = None
    
    def addNode(self, inse):       
        nde = Node(inse)      
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
    
    def addTwo(self, fi, se):
        self.head = None
        self.tail = None
        carry = 0
        
        while (fi is not None or se is not None):
            fdata = 0 if fi is None else fi.value
            sdata = 0 if se is None else se.value
            Sum = carry + fdata + sdata
        
            carry = 1 if Sum >= 10 else 0
        
            Sum = Sum if Sum < 10 else Sum % 10
        
            temp = Node(Sum)
        
            if self.head == None:
                self.head = temp
            else:
                self.tail.next = temp
            
            self.tail = temp
            
            if fi is not None:
                fi = fi.next
            if se is not None:
                se = se.next
                
        if carry > 0:       #for first digit = 1
            self.tail.next = Node(carry)        
        
def randomLinkedList(leng, min, max):
    from random import randint
    rll = LinkedList()
    for i in range(leng):
        value = randint(min, max)
        rll.addNode(value)
    return rll


l1 = randomLinkedList(3,0,9)
l2 = randomLinkedList(3,0,9)
print (l1)
print (l2)
res = LinkedList()
res.addTwo(l1.head, l2.head)
print (res)
