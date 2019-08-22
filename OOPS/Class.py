class test1:
    def add(self,a,b):
        print("test 1",a+b)
class test2(test1):
    def add(self,a,b):
        print('Test 2',a+b)
        super().add(20,30)
ob = test2()
ob.add(10,20)