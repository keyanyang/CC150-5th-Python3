class Node:
    def __init__(self, data, kind):
        self.data = data
        self.kind = kind
        self.next = None   
    
class ll:    
    def __init__(self):
        self.head = None
        self.tail = None
     
    def addAni(self, data, kind):
        node = Node(data, kind)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
       
    def enqueue(self, data, kind): 
        self.tail.next = Node(data, kind)
        self.tail = self.tail.next       
    
    def dequeueAny(self):
        if self.head != self.tail:
            self.head = self.head.next
        else:
            self.head = None
    
    def dequeueDog(self):       #pre and start
        pre = self.head
        start = self.head
        while(self.head != None):
            if self.head.kind == "dog":
                self.head = self.head.next
                return
            elif start.kind == "dog":
                pre.next = start.next
                return
            else:
                pre = start
                start = start.next   
        
    def printn(self):
        index = self.head
        while index != None:
            print(index.kind, 'born in', index.data)
            index = index.next

q = ll()   
q.addAni("89", "cat")
q.addAni("90", "cat")
q.addAni("93", "dog")
q.addAni("94", "dog")
q.addAni("91", "cat")
q.addAni("92", "cat")
q.printn()
print ("--------")
q.enqueue("95", "dog")
q.printn()
print ("--------")
q.dequeueAny()
q.dequeueAny()
q.dequeueAny()
q.dequeueAny()
q.printn()
print ("--------")
q.dequeueDog()
q.printn()
