from collections import deque

t = int(input())

def bfs(x, y):  
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while(queue):
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    matrix[nx][ny] = 2

for i in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)] 
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
