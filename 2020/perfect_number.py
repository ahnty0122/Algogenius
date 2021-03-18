# 완전수 : 자기 자신을 뺀 약수들의 합이 자기 자신과 같은 수
# 입력으로 n 받고 출력으로 n 이하의 모든 완전수 출력하기
# 모든 약수들은 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸
# 따라서 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨 ---- 약수를 먼저 찾고 해결

import math

def find_all_divisors_of_a_number(x):
	result = []
	for i in range(1, int(math.sqrt(x))+1):
		if x % i == 0:
			result.append(i)
			if i * i != x:
				result.append(x // i)
	return result

a, b = map(int, input().split())
for i in range(a, b+1):
	if sum(find_all_divisors_of_a_number(i)) - i == i:
		print(i, end = ' ')