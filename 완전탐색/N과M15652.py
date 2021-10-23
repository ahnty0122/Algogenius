import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []

def dfs(start):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(start, n+1):
        result.append(i)
        dfs(i)
        result.pop()
    
dfs(1)
