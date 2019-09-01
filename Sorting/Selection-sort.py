lis = [5,6,3,2,8,1]
for i in range(len(lis) - 1):
    minpos = i
    for j in range(i,len(lis)):
        if(lis[j] < lis[minpos]):
            minpos = j
    lis[i],lis[minpos] = lis[minpos],lis[i]
    print(lis)
print("final",lis)

