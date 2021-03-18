# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# ex) 00시 00분 03초, 00시 13분 30초는 세어야하는 시각

# 입력예시: 5
# 출력예시: 11475

h = int(input())

count = 0
for i in range(h+1):
	for j in range(60):
		for k in range(60):
			if '3' in str(i) + str(j) +str(k):
				count += 1

print(count)