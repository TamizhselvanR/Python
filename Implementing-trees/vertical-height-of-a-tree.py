class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.hd = 0
class BinaryTree():
    def __init__(self):
        self.root = None
    def create(self, val):
        current = self.root
        if current:
            while (True):
                if (val < current.info):
                    if (current.left):
                        current = current.left
                    else:
                        current.left = node(val)
                        break
                elif (val > current.info):
                    if (current.right):
                        current = current.right
                    else:
                        current.right = node(val)
                        break
        else:
            self.root = node(val)
def verticalheight(root):
    hd = 0
    sum = {}
    q = []
    root.hd = hd
    q.append(root)
    while (len(q)):
        n = q.pop(0)
        hd = n.hd
        if sum.get(hd) != None:
            sum[hd] += 1
        else:
            sum[hd] = 1
        if (n.left):
            n.left.hd = hd - 1
            q.append(n.left)
        if (n.right):
            n.right.hd = hd + 1
            q.append(n.right)
    for i in sorted(sum):
        print(i,sum[i])
lis = [5, 3, 2, 7, 6,9,8]
l = BinaryTree()
for i in lis:
    l.create(i)
verticalheight(l.root)