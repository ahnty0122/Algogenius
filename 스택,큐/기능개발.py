import math
def solution(progresses, speeds):
    answer = []
    left = []
    
    for i, j in zip(progresses, speeds):
        left.append(math.ceil((100 - i) / j))
    
    chk = left[0]
    count = 0
    for j in left:
        if chk < j:
            answer.append(count)
            chk = j
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))