class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
def treecheck(T1, T2):
    if T1 == T2 == None:
        return True
    elif T1 == None or T2 == None:      #without this command, it will show NoneType Error(None.data dosen't exist)
        return False
    elif T1.data != T2.data:
        return False
    else:
        return treecheck(T1.right, T2.right) and treecheck(T1.left, T2.left)
  
def findnode(T1, T2):
    if T2 == None:
        return True
    elif T1 == None:
        return False
    elif T1.data == T2.data:
        if treecheck(T1, T2):
            return True
    return findnode(T1.left, T2) or findnode(T1.right, T2)      #it must be 'or'

#test
t1 = Node(1, Node(2, Node(4, Node(4), Node(5)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
t2 = Node(3, Node(4), Node(5))
t3 = Node(3, Node(5), Node(5))
print (findnode(t1, t2))
print (findnode(t1, t3))
