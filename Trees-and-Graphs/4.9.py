class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
def findSum(node, givenSum, path=None, depth=0):        #add the value of nodes from bottom to top
    if node is None:
        return
    if path == None:
        path = []
    if len(path) > depth:
        path[depth] = node.value
    else:
        path.append(node.value)
    temp = 0
    for i in range(depth, -1, -1):
        temp += path[i]
        if temp == givenSum:
            printPath(path, i, depth + 1)
    findSum(node.left, givenSum, path, depth + 1)
    findSum(node.right, givenSum, path, depth + 1)

def printPath(path, start, end):
    for i in range(start, end):
        print(path[i], end = ' ')
    print('')

#test
t1 = Node(1, Node(2, Node(4, Node(4), Node(5)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
givenSum = 7
findSum(t1, givenSum)
