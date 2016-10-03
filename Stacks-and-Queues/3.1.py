# Single array for three stacks

class arrayStacks:
    def __init__(self, stacksize, n):       #set up pointer[-1, -1, -1] and array[None, None, ..., None]
        self.stacksize = stacksize
        self.n = n
        self.pointer = [-1] * self.n
        self.array = [None] * self.stacksize * self.n

    def stacktop(self, stacknum):
        return stacknum * self.stacksize + self.pointer[stacknum]

    def push(self, stacknum, value):
        if stacknum >= self.n:
            return 'stack number is out of space'
        elif self.pointer[stacknum] + 1 < self.stacksize:
            self.pointer[stacknum] += 1
            self.array[self.stacktop(stacknum)] = value
            return 'add {} in stack {}'.format(value, stacknum)
        else:
            return 'out of space'
    
    def pop(self, stacknum):
        if stacknum >= self.n:
            return 'stacknumber is out of space'
        elif self.pointer[stacknum] < 0:
            return 'this stack is empty and cannot be popped'
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return 'remove {} in stack {}'.format(data, stacknum)
        
    def showTop(self, stacknum):
        if self.pointer[stacknum] < 0:
            return 'empty stack'
        else:
            return '{} is the latest value in stack {}'.format(self.array[self.stacktop(stacknum)], stacknum)
    
    def showArray(self):
        return self.array    
    
array = arrayStacks(10,3)       #array=[None,...None] where there is 30 Nones
print (array.push(2, 20))       #In stack2, the first value is 20
print (array.push(2, 30))       #In stack2, the next value is 30
print (array.push(4, 30))       #no stack4  
print (array.pop(1))        #remove and show the latest value of stack 1, which should be empty 
print (array.pop(2))        #remove and show the latest value of stack 2           
print (array.showTop(2))        #show the current first value of stack2 
print (array.push(2, 10))
print (array.showTop(2)) 
print (array.push(0, 20))
print (array.push(0, 30))
print (array.showArray())       #show this array which includes three stacks
