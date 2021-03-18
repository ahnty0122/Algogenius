# 7
# 7 1 5 9 6 7 3



# O(n) 방법으로 sum 구하기
'''
sum=0
for i in range(1,n+1,1):
	sum+=i
print(sum)
'''



import sys
sys.setrecursionlimit(2000)

# O(logN)
def fastSum(n): # 7 6 3 2 1
	#기저사건
	if n==1:
		return 1
	# 짝수 홀수
	if n%2==1:
		return fastSum(n-1) + n
	return 2*fastSum(n/2)+(n/2)*(n/2)
print(fastSum(10))