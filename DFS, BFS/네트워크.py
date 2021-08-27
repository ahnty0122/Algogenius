def dfs(computers, visited, start):
    record = [start]
    while record:
        j = record.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(0, len(computers)):
            if computers[j][i] == 1 and visited[i] == 0: # 연결되어 있으면 record에 추가
                record.append(i)
                    
def solution(n, computers):
    answer = 0
    visited = [0] * n # 방문확인
    start = 0
    while 0 in visited: # 방문 안 된 노드 있으면 계속
        if visited[start] == 0:
            dfs(computers, visited, start) # 방문
            answer += 1
        start += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
# 1

'''
def dfs(visited, computers, v):
    visited[v] = 1
    for i in range(len(computers[v])):
        if visited[i] == 0 and computers[v][i] == 1:
            dfs(visited, computers, i)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(visited, computers, i)
            answer += 1
        if 0 not in visited:
            break
    return answer
'''