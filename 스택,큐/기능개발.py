import math
def solution(progresses, speeds):
    answer = []
    days = []
    
    for i, j in zip(progresses, speeds):
        days.append(math.ceil((100 - i) / j))
    
    chk = days[0]
    count = 0
    for j in days:
        if chk < j:
            answer.append(count)
            chk = j
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))