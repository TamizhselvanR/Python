'''

Given a number N followed by an unsorted array of N numbers and a number K, find if there exists a pair of elements in the array whose difference is K. Return count of such pairs.
Example k=4 and a[]={7,6,23,19,10,11,9,3,15}
Output should be : 6
Pairs can be:
7,11
7,3
6,10
19,23
15,19
15,11
Input Size : N <= 100000
Sample Testcase :
INPUT
6 4
8 12 16 4 0 20
OUTPUT
5

'''

from itertools import combinations
n,k = map(int,input().rstrip().split())
lis = list(map(int,input().rstrip().split()))
lis.sort()
lis = lis[::-1]
count = 0
for i,j in combinations(lis,2):
 if(i - j == k):
  count += 1
print(count)