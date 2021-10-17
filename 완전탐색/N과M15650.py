# from itertools import combinations, islice
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)
 

# for i in combinations(s, m):
#     for j in i:
#         print(j, end = " ")
#     print()