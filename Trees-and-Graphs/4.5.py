#binary tree python
class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

#implement a function if a binary tree is a binary search tree

def in_order_search(btree):     #make it list        #[] + [1] = [1]
    if btree is None: return []
    return in_order_search(btree.left) + [btree.content] + in_order_search(btree.right)
    

def valid_bsearch_tree(btree):
    if btree is None: return True
    l = in_order_search(btree) 
    if sorted(l) == l:return True
    return False

from random import randint
def make_random_btree(depth = 2):
    if depth <= 0: return None
    tree = BinaryTree(randint(0,10))
    tree.left = make_random_btree(depth - 1)
    tree.right = make_random_btree(depth - 1)
    return tree

def make_random_bsearch_tree(depth = 2, l = -10, r = 10):
    if depth <= 0 or l == r: return None
    tree = BinaryTree(randint(l, r))
    tree.left = make_random_bsearch_tree(depth - 1, l, tree.content)
    tree.right = make_random_bsearch_tree(depth - 1, tree.content, r)
    return tree

def btl(bt):        #just for looking the binary tree/search tree better! not necessary
    if bt == None:
        return []
    ret = [[bt.content]]
    queue = [bt]
    while len(queue) > 0:
        nq = []
        for node in queue:
            if node.left != None:
                nq.append(node.left)
            if node.right != None:
                nq.append(node.right)
        queue = nq
        if len(queue) == 0:
            break
        ret.append([x.content for x in nq])
    return ret    

bt = make_random_btree(4)
bst = make_random_bsearch_tree(3)
#test1
print (bt)
print (btl(bt))
print (in_order_search(bt))
print (valid_bsearch_tree(bt))
print (bst)
print (btl(bst))
print (in_order_search(bst))
print (valid_bsearch_tree(bst))
