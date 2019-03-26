'''

The first line contains an integer, , the number of students who have subscribed to the English newspaper.
The second line contains space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains space separated roll numbers of those students.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

13

'''

n1 = int(input())
s1 = set(input().split())
n2 = int(input())
s2 = set(input().split())
print(len(s1.union(s2)))'''printing the number of students who have subscribed to atleast one paper'''
