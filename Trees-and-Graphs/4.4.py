class bTree:
    def __init__(self, content, left, right):
        self.content = content 
        self.right = right
        self.left = left
    
    def __str__(self):
        return '(' + str(self.content) + '(' + str(self.left) + '|' + str(self.right) + '))'
    
class linkedList:
    def __init__(self, content):
        self.content = content
        self.next = None
    
    def __str__(self):
        if self.next == None:
            return str(self.content)
        else:
            return str(self.content) + '-' + str(self.next)
        
def btll(bt, depth = 1, nodeonlevel = []):
    if len(nodeonlevel) >= depth:
        ll = linkedList(bt.content)
        ll.next = nodeonlevel[depth - 1]
        nodeonlevel[depth - 1] = ll
    else:
        nodeonlevel.append(linkedList(bt.content))
    if bt.left != None:
        nodeonlevel = btll(bt.left, depth + 1, nodeonlevel)
    if bt.right != None:
        nodeonlevel = btll(bt.right, depth + 1, nodeonlevel)
    return nodeonlevel

#test
import random
def makebt(depth):
    if depth <= 0:
        return None
    else:
        return bTree(random.randrange(0,100), makebt(depth - 1), makebt(depth - 1))

bt1 = makebt(4)
print(bt1)
print ('-------------------------------------')
for ll in btll(bt1):
    print(ll)
    
    
        
