class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

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

def randomLinkedList(leng, min, max):
    from random import randint
    rll = LinkedList()
    for i in range(leng):
        value = randint(min, max)
        rll.addNode(value)
    return rll

def isPalindrome(ll):
    if ll.head == None:
        return None
    fast = ll.head
    slow = ll.head
    firsthalf = []
    while fast != None and fast.next != None:
        firsthalf.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
        slow = slow.next
    while slow != None:
        if firsthalf.pop() != slow.value:
            return False
        else:
            slow = slow.next
    return True
    
            
for i in range(20):               
    test = randomLinkedList(5, 3, 5)
    print (test)
    print (isPalindrome(test))

