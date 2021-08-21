n = int(input())

visited = [[0] * (n) for _ in range(n)]
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, visited, x, y):
    visited[x][y] = 1
    global count
    if graph[x][y] == 1:
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(graph, visited, nx, ny)

num_home = []
count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(graph, visited, i, j)
            num_home.append(count)
            count = 0

print(len(num_home))
for i in sorted(num_home):
    print(i)

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''