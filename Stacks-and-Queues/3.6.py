class Stack(list):
    def push(self, value):
        self.append(value)
    
    def isEmpty(self):
        return self == []
    
    def peak(self):
        return self[-1]
    
    def sort(s1):      
        s2 = Stack()        #s2 is new stack
        while s1 != []:
            cur = s1.pop()
            while s2 != [] and s2.peak() > cur:
                s1.push(s2.pop())
            s2.push(cur)
            while s1 != [] and s1.peak() >= s2.peak():
                s2.push(s1.pop())
        return s2

from random import randrange
items = [randrange(50) for i in range(20)]
s = Stack()
for i in items:
    s.push(i)
print(s)
s2 = Stack.sort(s)
print(s2)
