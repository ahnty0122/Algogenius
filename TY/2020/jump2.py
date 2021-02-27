# NxN 게임판, 가장 왼쪽 위칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프
# 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리
# 칸 이동 시 반드시 오른쪽이나 아래쪽
# 0은 더 이상의 진행을 막는 종착점
# 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야함
# 가장 왼쪽 위 칸에서 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수 구하기

n = int(input())
board=[[int(i) for i in input().split(' ')] for j in range(n)]
dp = [[0 for i in range(n)] for i in range(n)]
dp[0][0] = 1
for i in range(n):
	for j in range(n):
		if i == 0 and j == 0:
			continue
		for k in range(j):
			if k + board[i][k] == j:
				dp[i][j] += dp[i][k]
		for k in range(i):
			if k + board[k][j] == i:
				dp[i][j] += dp[k][j]
print(dp[n-1][n-1])

'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
'''

'''
3
'''

'''
다른방법
countCache=[[-1 for i in range(101)]for j in range(101)]
def path(y,x):
    if y>=7 or x>=7:
        return 0
    if y==6 and x==6:
        return 1
    tmp=cache[y][x]
    if tmp!=-1:
        retrun tmp
    jumpSize=board[y][x]
    tmp=path(y+jumpSize,x) or path(y,x+jumpSize)
    return tmp

def count(y,x):
    if y==n-1:
        return 1
    tmp=countCache[y][x]
    if tmp!=-1:
        return tmp
    tmp=0
    if path(y+1,x+1) >= path(y+1,x):
        tmp+=count(y+1,x+1)
    if path(y+1,x+1) <= path(y+1,x):
        tmp+=count(y+1,x)
    return tmp
'''