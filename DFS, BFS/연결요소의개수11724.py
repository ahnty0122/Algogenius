import sys
sys.setrecursionlimit(10 ** 6) # python 재귀 제한
read = sys.stdin.readline

n, m = map(int, read().split())
graph = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(m):
    a, b = map(int, read().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (n + 1)
count = 0

def dfs(v, visited):
    visited[v] = 1
    for i in range(n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i, visited)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i, visited)
        count += 1

print(count)

