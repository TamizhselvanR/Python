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
def preorder(root):
    if root:
        print(str(root.info), end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.info), end=" ")
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.info), end=" ")
        inorder(root.right)
lis = [5, 3, 2, 7, 6]
l = BinaryTree()
for i in lis:
    l.create(i)
preorder(l.root)
postorder(l.root)
inorder(l.root)



