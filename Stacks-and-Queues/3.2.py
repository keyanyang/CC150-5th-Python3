class smin():
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        data = self.stack.pop()
        if data == self.min[-1]:
            self.min.pop()
        return data
    
    def getmin(self):
        if len(self.min) == 0:
            return None
        print (self.min[-1])
    
s = smin()
from random import randrange
ranlist = [randrange(100) for i in range(10)]
for num in ranlist:
    s.push(num)
print (s.stack)
s.getmin()    
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print (s.stack)     #after a few pops, to see the list and the min
s.getmin()
    
