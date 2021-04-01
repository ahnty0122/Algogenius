def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    a_count = 0
    b_count = 0
    c_count = 0
    for i, ans in enumerate(answers):
        if a[i] == ans:
            a_count += 1
        if b[i] == ans:
            b_count += 1
        if c[i] == ans:
            c_count += 1
    final = [a_count, b_count, c_count]
    for i, j in enumerate(final):
        if j == max(final):
            answer.append(i + 1)
    return answer
print(solution([1,3,2,4,2]))