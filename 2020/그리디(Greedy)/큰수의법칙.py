n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort() # 입력받은 수들 정렬하기
first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 두번째로 큰 수

while True:
	for i in range(k):
		if m == 0:
			break
		result += first
		m -= 1
	if m == 0:
		break
	result += second
	m -= 1

print(result)