class BTreeNode:
    def __init__(self, isLeaf = False) -> None:
        self.isLeaf = isLeaf
        self.keys = []  # Empty List to append to later
        self.chilren = []
        

class BTree:
    def __init__(self, m) -> None:
        self.m = m  # key
        self.root = BTreeNode(isLeaf = True)

    def insert(self, x, k):
        # Start by insertingm regardless of overflow
        n = len(x.keys) - 1 
        i = 0
        if (x.isLeaf == True):
            #Add to the leaf nodes.
            x.keys.append(None) # Make room
            while i <= n and x.keys[n]< k: # Linear Scan
                x.keys[i] = x.keys[i+1]
                i += 1
            x.keys[i + 1] = k
        else:   # Root Node, so we need to see where to add it
            while i <= n and x.keys[n]< k: # Linear Scan
                i += 1
            x.keys[i+1] = k
            # Now that we have inserted k, we need to look at the right neighbor.
            i +=1
            if len(x.children[i].keys) == (2 * self.m):
                #Overflow 
                self.checkOverflow(x,i)

    def checkOverflow(self, x, i):
        m = self.m
        tmp = x.children[i]
        right = BTreeNode(leaf = tmp.leaf)
        left = BTreeNode(True)
        right.keys = tmp[m : (2 * m) -1]
        left.keys = tmp[0:m-1]
        if tmp.leaf == False:   #Median Root Node
            right.keys = tmp[m : (2 * m)]
            left.keys = tmp[0:m-1]