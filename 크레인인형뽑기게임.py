def solution(board, moves):
    answer = []
    out = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                out.append(board[j][i-1])
                board[j][i-1] = 0
                if out[-1:] == out[-2:-1]:
                    answer.append(out[-1:])
                    out = out[:-2]
                break
    return len(answer)*2

# index range 고려하기
# out list에 append 후 board 값 0으로 초기화 시켜주기
# list 맨 마지막과 마지막에서 두번째 값 비교 --> 슬라이싱 활용 [-1:] [-2:-1]