class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

def find_next_btree(bt):            #take the example of a 9-nodes binary search tree, choose node 0 and node 3
    if bt is None: return None
    if bt.right is None:
        ret = bt.parent
        while ret is not None and ret.content <= bt.content:
            ret = ret.parent
        return ret
    else:
        ret = bt.right
        if ret.left is not None:
            ret = ret.left
        return ret

#test
from random import randrange
def make_random_bsearch_tree(depth = 2, l = -10, r = 10, parent = None):
    if depth < 0 or l == r: return None
    tree = BinaryTree(randrange(l, r))
    tree.parent = parent
    tree.left = make_random_bsearch_tree(depth - 1, l, tree.content, tree)
    tree.right = make_random_bsearch_tree(depth - 1, tree.content, r, tree)
    return tree

def btl(bt):        #just for observing the bst better
    if bt == None: return []
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
        ret.append([x.content for x in queue])
    return ret
            
    
def in_order_check(btree):
    if btree is None: return None
    in_order_check(btree.left)
    print('current node', btree.content)
    next_node = find_next_btree(btree)
    if next_node is None:
        return None
    else:
        print('->next node', next_node.content)
    in_order_check(btree.right)

tree = make_random_bsearch_tree()
print (tree)
print(btl(tree))
in_order_check(tree)
