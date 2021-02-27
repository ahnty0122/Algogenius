# 삼각형 위의 최대 경로
# 맨 위에서 시작해 한칸씩 아래로 내려가 맨 아래줄까지 닿는 경로 만들 때
# 만들어지는 경로의 숫자의 합이 최대화되는 경로의 최대합 구하기
# 아래 또는 오른쪽 숫자로만 움직일 수 있음

n=int(input())
tri=[[int(i) for i in input().strip().split(" ")] for j in range(n)]
cache=[[-1 for i in range(n)] for j in range(n)]
def path(y,x):
	if y==n-1:
		return tri[y][x]
	tmp=cache[y][x]
	if tmp!=-1 :
		return tmp
	return max(path(y+1,x),path(y+1,x+1))+tri[y][x]

print(path(0,0))

''' 입력예시
5 #몇줄인지 나타내는 자연수
6 #삼각형 숫자들 출력
1 2
3 7 4
9 4 1 7
2 7 5 9 4
'''

''' 출력예시
28
'''