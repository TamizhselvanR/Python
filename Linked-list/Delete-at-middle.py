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
    def dele(self,fin):
        current =self.root
        while(current.info != fin):
            pre = current
            current = current.next
        print(current.info)
        pre.next = current.next
def printe(root):
    current = root
    while current:
        print(str(current.info),end = " ")
        current = current.next
lis = [5, 3, 2, 7, 6]
l = linkedlist()
for i in lis:
    l.create(i)
l.dele(3)
printe(l.root)


