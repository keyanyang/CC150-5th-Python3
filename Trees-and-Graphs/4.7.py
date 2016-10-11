class bTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
    
    def __str__(self):
        return '(' + str(self.content) + '(' + str(self.left) + '|' + str(self.right) + '))'

import random
def makebt(depth, p = None):
    if depth <= 0: return None
    bt = bTree(random.randrange(0,20))
    bt.parent = p
    bt.left = makebt(depth - 1, bt)
    bt.right = makebt(depth - 1, bt)
    return bt


def common(node1, node2):
    node1.color = "mark"
    while node1.parent != None:
        node1.parent.color = "mark"
        node1 = node1.parent
    node1.color = "mark"
    while node2.parent != None:
        if node2.color == "mark":
            return(node2.content)
        node2 = node2.parent
    if node2.color == "mark":
        return(node2.content)       
#
bt1 = makebt(5)
print(bt1)
node1 = bt1.left.left
node2 = bt1.right.right
commonancestor = common(node1, node2)
print('first common ancestor of two nodes, {} and {}, is: {}'.format(node1.content, node2.content, commonancestor))

