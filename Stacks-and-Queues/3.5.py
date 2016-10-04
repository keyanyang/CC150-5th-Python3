class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, num):
        self.stack1.append(num)
        del self.stack2[:]
        i = 1
        while i <= len(self.stack1):
            self.stack2.append(self.stack1[-i])
            i += 1
    
    def pop(self):
        return self.stack2.pop()

mq = MyQueue()
print (mq.stack1, mq.stack2)    
mq.push(1)
mq.push(2)
mq.push(3)
mq.push(4)
print (mq.stack1, mq.stack2) 
mq.push(50)
mq.push(100)
print (mq.stack1, mq.stack2) 
print (mq.pop())
print (mq.pop())
print (mq.pop())
print (mq.stack1, mq.stack2)    #FIFO
