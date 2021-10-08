# 서로 인접한 정점이 같은 색이면 이분 그래프 X

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a] # i와 연결된 정점을 -로 바꿔줌 (이분그래프)
                q.append(i)
            else:
                if visited[i] == visited[a]:
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    flag = True
    graph = [[] for i in range(v + 1)]
    visited = [0 for i in range(v + 1)]
    
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for k in range(1, v + 1):
        if visited[k] == 0:
            if not bfs(k):
                flag = False
                break

    print("YES" if flag else "NO")