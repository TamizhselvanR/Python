lis = [5,3,8,6,6,7,2]
for i in range(len(lis)-1,0,-1):
    count = 0
    for j in range(i):
        if(lis[j] > lis[j+1]):
            lis[j],lis[j+1] = lis[j+1],lis[j]
print(lis)