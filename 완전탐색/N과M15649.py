import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()

# for i in result:
#     print(i)

# permutations 이용 방법
# import sys
# input = sys.stdin.readline
# from itertools import permutations

# n, m = map(int, input().split())
# s = [(i + 1) for i in range(n)]
# for i in permutations(s, m):
#     for j in list(i):
#         print(j, end = " ")
#     print()