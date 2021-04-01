def solution(v, len):
    answer = []
    right = [v[0][1], v[1][1], v[2][1]]
    left = [v[0][0], v[1][0], v[2][0]]
    for j in left:
        if left.count(j) == 1:
            answer.append(j)
            break
    for i in right:
        if right.count(i) == 1:
            answer.append(i)
    return answer

print(solution([[1, 4], [3, 4], [3, 10]], 3))