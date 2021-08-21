n = int(input())
m = int(input())

matrix = [[0] * (n + 1) for i in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def dfs(graph, visited, v):
    visited[v] = 1
    global count
    for i in range(n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(graph, visited, i)
            count += 1

count = 0
dfs(matrix, visited, 1)
print(count)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''