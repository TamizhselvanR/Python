n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in arr:
    for j in arr:
        result += abs(i-j)**k
print(result)