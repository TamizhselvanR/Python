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
    def insbef(self,val,bef):
        current =self.root
        while(current.info != bef):
            pre = current
            current = current.next
        after = current.next
        current.next = node(val)
        current.next.next = after
def printe(root):
    current = root
    while current:
        print(str(current.info),end = " ")
        current = current.next
lis = [5, 3, 2, 7, 6]
l = linkedlist()
for i in lis:
    l.create(i)
l.insbef(9,2)
printe(l.root)