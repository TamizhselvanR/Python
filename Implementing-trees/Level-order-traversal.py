from __future__ import print_function
class node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
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
def levelOrder(root):
    if root is not None:
        q = [root]
        while(len(q) > 0):
            n = q.pop(0)
            print(str(n.info),end = " ")
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
lis = [5, 3, 2, 7, 6]
l = BinaryTree()
for i in lis:
    l.create(i)
levelOrder(l.root)