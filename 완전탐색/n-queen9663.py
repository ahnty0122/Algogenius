def dfs(queen, n, row):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for x in range(row):
            if queen[x] == queen[row]: # 같은 열에 있으면 안됨 
                break
            # 대각선에 있으면 안됨
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)
    return count

def solution(n):
    queen = [0] * n
    # 각 열에서 퀸의 위치 (인덱스가 행, 값이 열)
    return dfs(queen, n, 0)