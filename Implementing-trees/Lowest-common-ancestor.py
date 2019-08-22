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
def lca(root,v1,v2):
    while(True):
        if(v1 < root.info and v2 < root.info):
            root = root.left
        elif(v1 > root.info and v2 > root.info):
            root = root.right
        else:
            return root.info

lis = [5, 3, 2, 7, 6]
l = BinaryTree()
for i in lis:
    l.create(i)
print(lca(l.root,2,6))
