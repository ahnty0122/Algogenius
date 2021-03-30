from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(i, j) for j, i in enumerate(priorities)])
    while d:
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
# 5