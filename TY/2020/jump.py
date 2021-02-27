# 7 x 7 격자 1~9 정수
# 1. 맨 왼쪽 위에서 맨 오른쪽 아래까지 도달하면 1
#    도달하지 못하면 0
# 2. 각 칸에 적혀진 숫자 만큼만 움직일 수 있다. 
# 3. 오른쪽 또는 왼쪽
# 4. 게임판 밖으로 벗어날 수 없다.
cache=[[-1 for i in range(7)] for j in range(7)]
board=[[int(i) for i in input().split(' ')] for j in range(7)]
def jump(y,x):
    if y>=7 or x>=7:
        return 0
    if y==6 and x==6:
        return 1
    tmp=cache[y][x]
    if tmp!=-1:
        retrun tmp
    jumpSize=board[y][x]
    tmp=jump(y+jumpSize,x) or jump(y,x+jumpSize)
    return tmp

'''
입력예시
2 5 1 6 1 4 1
6 1 1 2 2 9 3
7 2 3 2 1 3 1
1 1 3 1 7 1 3
4 1 2 3 4 1 3
3 3 1 2 3 4 1
1 5 2 9 4 7 0

출력예시
0
'''

