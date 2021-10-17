import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0] * (n + 1)

result = []

def dfs():
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(1, n+1):
        result.append(i)
        dfs(i)
        result.pop()
    
dfs()
