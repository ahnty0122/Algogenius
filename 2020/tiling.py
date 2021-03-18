# tile(n) = tile(n-1) + tile(n-2)
# n 타일 개수 - 대칭 = 비대칭 
# 2xn 크기의 직사각형을 2x1 크기의 타일로 채움
# 2x1 타일을 회전해서 쓸 수 있음
# 해당 타일 배치는 좌우대칭이면 안될 때 타일을 채우는 경우의 수

cache=[-1 for i in range(21)]
def tile(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if cache[n] != -1:
        return cache[n]
    return tile(n-1)+tile(n-2)
n=int(input())
if n%2==1 :
    print(tile(n)-tile(n//2))
else :
    print(tile(n)-tile(n//2)-tile(n//2-1))