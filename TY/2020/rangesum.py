# dp로 풀어보기

n=int(input())
dp=[[0]*n for _ in range(n)]

lst=list(map(int,input().split()))
for i in range(n):
	dp[i][i]=lst[i]
a,b=map(int,input().split())
for i in range(n):
	for j in range(i+1,n):
		dp[i][j]=dp[i][j-1]+lst[j]
print(dp[a-1][b-1])

# 더 간단하게 풀어보기

n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
result=0
for i in range(a-1,b):
	result+=lst[i]
print(result)
