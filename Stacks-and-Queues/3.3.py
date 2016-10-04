class SetOfStacks:
    def __init__(self, capacity):
        self.stack = []
        self.cap = capacity
    
    def push(self, value):
        if len(self.stack) == 0 or len(self.stack[-1]) == self.cap:
            self.stack.append([])
        self.stack[-1].append(value)
        
    def pop(self):
        if len(self.stack) == 0:
            print ('empty stack cannot be popped')
        else:
            if len(self.stack[-1]) == 0:
                self.stack.pop()
            self.stack[-1].pop()
        
    def popAt(self, index):
        if index < 0 or index > (len(self.stack)-1) or len(self.stack[index]) == 0:
            print ('index should be within capacity and larger than 0, and empty substack cannot be popped')
        else:
            return self.stack[index].pop()
        
#test    
stacks = SetOfStacks(5)
stacks.pop()        #try to pop when the stack is none
for i in range(17):
    stacks.push(i)
print(stacks.stack)

stacks.pop()
print(stacks.stack)  
stacks.pop()
print(stacks.stack)
stacks.popAt(3)     #try to pop at empty substack  
stacks.pop()
print(stacks.stack)  

stacks.popAt(0)
print(stacks.stack)  
