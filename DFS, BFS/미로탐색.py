from sys import stdin

N, M = map(int, stdin.readline().split())

matrix = [stdin.readline().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
# queue 
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

'''
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# �ʺ� �켱 Ž��
def bfs(x, y):
  # �̵��� �� ���� ���� ���� (��, ��, ��, ��)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque ����
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # ���� ��ġ���� 4���� �������� ��ġ Ȯ��
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # ��ġ�� ����� �ȵǱ� ������ ���� �߰�
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      # ���̹Ƿ� ���� �Ұ�
      if graph[nx][ny] == 0:
        continue
      
      # ���� �ƴϹǷ� �̵�
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # ������ ������ ī��Ʈ ���� �̴´�.
  return graph[N-1][M-1]

print(bfs(0, 0))
'''

'''
4 6
101111
101010
101011
111011
'''