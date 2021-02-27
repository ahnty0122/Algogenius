# 여행가 A가 NxN 크기의 정사각형 공간에서 움직임
# 입력: 공간의 크기가 주어지는 N이 첫째줄에 주어지고 (1<=N<=100)
#  	    여행가 A가 이동할 계획서 내용이 둘째줄에 주어짐 (1<=이동횟수<=100)
# 출력: 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백을 기준으로 구분해 출력
# 공간을 벗어나는 움직임은 무시됨

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
	# 이동 후 좌표 구하기
	for i in range(len(move_types)):
		if plan == move_types[i]:
			nx = x + dx[i]
			ny = y + dy[i]
	# 공간을 벗어나는 경우 무시
	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue
	x, y = nx, ny

print(x, y)