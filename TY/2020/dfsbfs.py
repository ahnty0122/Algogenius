N, M, V = map(int, input().split())
matrix = [[0 for i in range(N+1)] for j in range(N + 1)]
for i in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

def dfs(current_node, row, visited):
    visited += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in visited:
            visited = dfs(search_node, row, visited)
    return visited

def bfs(start):
    queue = [start]
    visited = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visited:
                visited += [search_node]
                queue += [search_node]
    return visited


print(*dfs(V, matrix, []))
print(*bfs(V))

