from collections import deque

def bfs(graph, start, visited):
	queue = deque()
	# 현재 노드 방문 처리
	visited[start] = True
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end = ' ')
		# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 2차원 리스트로 graph 표현
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = False * 9

bfs(graph, 1, visited)