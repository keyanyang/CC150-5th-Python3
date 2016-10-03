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

def findLoop(ll):
    slow = ll.head
    fast = ll.head
    
    while (fast != None) and (fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    
    if fast == None or fast.next == None:
        return None
    
    fast = ll.head
    while fast != slow:
        fast = fast.next
        slow = slow.next
        
    return fast.value

#test
l = LinkedList()
cur = l.head
store = []
rg = 10
loopbegin = 2

for i in range(rg):
    l.addNode(i)
    if i == 0:
        cur = l.head
    else:
        cur = cur.next
    store.append(cur)

cur.next = store[loopbegin]

print ('When the number of elements is {} and the beginning of loop is {}, we can find the beginning loop is'.format(rg, loopbegin))
print (findLoop(l))


    
            
                

