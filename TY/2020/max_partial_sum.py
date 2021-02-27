# 최대 부분합 구하기 동적계획법

n = int(input())
arr = [int(input()) for i in range(n)]

def result(arr):
	cache = [0] * len(arr)
	cache[0] = arr[0]
	for i in range(0, len(arr)):
			cache[i] = max(0, cache[i-1]) + arr[i]
	return max(cache)

print(result(arr))