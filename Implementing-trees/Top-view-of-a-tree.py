from __future__ import print_function
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
def topview(root):
    m = dict()
    hd = 0
    root.hd = hd
    q = []
    q.append(root)
    while (len(q)):
        n = q[0]
        hd = n.hd
        if hd not in m:
            m[hd] = n.info
            if (n.left):
                n.left.hd = hd - 1
                q.append(n.left)
            if (n.right):
                n.right.hd = hd + 1
                q.append(n.right)
        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")
lis = [5, 3, 2, 7, 6]
l = BinaryTree()
for i in lis:
    l.create(i)
topview(l.root)