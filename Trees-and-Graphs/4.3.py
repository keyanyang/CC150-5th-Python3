class bTree:
    def __init__(self, content, left, right):
        self.content = content
        self.left = left
        self.right = right
    
    def __str__(self):
        return '(' + str(self.content) + '(' + str(self.left) + '|' + str(self.right) +'))'
    
def atb(inta):
    if inta == []:
        return None
    elif len(inta) == 1:
        return inta[0]
    else:
        cut = len(inta) // 2
        return bTree(inta[cut], atb(inta[0:cut]), atb(inta[cut+1:]))

ia = [1,2,3,4,5,6,8,10,20,50,100,200]
print (atb(ia))
