class bTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if node == None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1
    
def balance(bt):
    if bt == None:
        return True
    else:
        return balance(bt.left) and balance(bt.right) and abs(height(bt.left) - height(bt.right)) <= 1

BT1 = bTree(1, bTree(2, bTree(4), bTree(5)), bTree(3))    
print('The height of leftsubtree:')
print(height(BT1.left))
print('The height of rightsubtree:')
print(height(BT1.right))
print('Is is balenced?')
print(balance(BT1))
print('-------------')
BT2 = bTree(1, bTree(2, bTree(4, bTree(6), bTree(7)), bTree(5)), bTree(3))    
print('The height of leftsubtree:')
print(height(BT2.left))
print('The height of rightsubtree:')
print(height(BT2.right))
print('Is is balenced?')
print(balance(BT2))
