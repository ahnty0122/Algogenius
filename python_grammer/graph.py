graph = [[0] * (n) for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().strip()
    for j, b in enumerate(line):
        graph[i][j] = int(b)


graph = []
for _ in range(n):
   graph.append(list(input()))


graph = [list(map(int, list(input()))) for _ in range(n)]
