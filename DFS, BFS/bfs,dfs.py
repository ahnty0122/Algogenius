from collections import deque
import sys
read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = [[0 for i in range(n + 1)] for j in range(n + 1)]

visited_d = [0] * (n + 1)
visited_b = [0] * (n + 1)

for i in range(m):
    a, b = map(int, read().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(visited, graph, v):
    visited[v] = 1
    print(v, end = " ")
    for i in range(n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(visited, graph, i)

def bfs(visited, graph, v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while(queue):
        v = queue.popleft()
        print(v, end = " ")
        for i in range(n + 1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1

dfs(visited_d, graph, v)
print()
bfs(visited_b, graph, v)

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''