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

#with hash table, change node's next
def deleteD1(ll):
    if (ll.head != None):
        currNode = ll.head
        dic =  {currNode.value: True}
        while currNode.next != None:
            if currNode.next.value in dic:
                currNode.next = currNode.next.next
            else:
                dic[currNode.next.value] = True
                currNode = currNode.next
                
#temp buffer is not allowed, node's next is changed
def deleteD2(ll):
    outer = ll.head
    while outer != None:
        inner = outer
        while inner.next != None:
            if inner.next.value == outer.value:
                inner.next = inner.next.next
            else:
                inner = inner.next
        outer =outer.next
                
test = randomLinkedList(5, 6, 10)
print (test)
print ("remove duplicates with hash table")
deleteD1(test)
print (test)
print ("remove duplicates without data structure")
deleteD2(test)
print (test)
