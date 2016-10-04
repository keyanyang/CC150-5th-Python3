class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, num):
        self.stack1.append(num)
        l = len(self.stack2) + 1
        del self.stack2[:]
        i = 1
        if l <= 0:
            self.stack2.append(self.stack1[-i])
        else:
            while i <= l:
                self.stack2.append(self.stack1[-i])
                i += 1
    
    def pop(self):
        return 'pop {}'.format(self.stack2.pop())

mq = MyQueue()
print (mq.stack1, mq.stack2)    
mq.push(1)
print (mq.stack1, mq.stack2)    
mq.push(2)
print (mq.stack1, mq.stack2)    
mq.push(3)
print (mq.stack1, mq.stack2)   
mq.push(4)
print (mq.stack1, mq.stack2) 
mq.push(50)
mq.push(100)
print (mq.stack1, mq.stack2) 
print (mq.pop())
print (mq.pop())
print (mq.pop())
print (mq.stack1, mq.stack2)    #FIFO
mq.push(3)
print (mq.stack1, mq.stack2)
mq.push(4)
print (mq.stack1, mq.stack2)
