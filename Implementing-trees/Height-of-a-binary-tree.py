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
def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return max(left,right) + 1
lis = [5, 3, 2, 7, 6]
l = BinaryTree()
for i in lis:
    l.create(i)
print(height(l.root))