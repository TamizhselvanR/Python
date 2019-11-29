class node:
    def __init__(self,info):
        self.info = info
        self.next = None
class linkedlist():
    def __init__(self):
        self.root = None
    def create(self, val):
        current = self.root
        if current is None:
            self.root = node(val)
        else:
            while current.next:
                current = current.next
            current.next = node(val)
def printe(root):
    current = root
    while current:
        print(str(current.info),end = " ")
        current = current.next
def reverse(root):
    current = root
    prev = None
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

lis = [5, 3, 2, 7, 6]
l = linkedlist()
for i in lis:
    l.create(i)
l.root = reverse(l.root)
printe(l.root)


