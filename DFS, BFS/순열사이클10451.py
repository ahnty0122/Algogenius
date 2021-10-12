import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())

def dfs(v):
    visited[v] = 1 
    next = m[v]
    if visited[next] == 0:
        dfs(next)

for i in range(t):
    n = int(input())
    visited = [0] * (n + 1)
    m = [0] + list(map(int, input().split()))
    
    cnt = 0
    for j in range(1, n + 1):
        if visited[j] == 0:
            dfs(j)
            cnt += 1
    print(cnt)