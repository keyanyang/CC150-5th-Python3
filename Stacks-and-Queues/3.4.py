class Hanoi:
    def __init__(self, size):
        self.towers = [[],[],[]]
        self.size = size
        self.towers[0] = [i for i in range(size, 0, -1)]        #size 1 is the smallest size
    
    def moveDisks(self, size, fr, helper, to):
        if size == 1:
            data = self.towers[fr].pop()
            self.towers[to].append(data)
            print ('Disk {} from Tower{} to Tower{}'.format(data, fr, to))
        else:
            self.moveDisks(size - 1, fr, to, helper)
            self.moveDisks(1, fr, helper, to)
            self.moveDisks(size - 1, helper, fr, to)
    
    def start(self):        #build this func to ensure size in moveDisks is the same as size in __init__
        print (h.towers)
        h.moveDisks(self.size, 0, 1, 2)
        print (h.towers)       

h = Hanoi(5)
h.start()
