def solution(a, b):
    answer = 0
    size = 0
    chk = ''
    while(len(chk.join(b) + " " * size) <= len(a)):
        chk = ' ' * size
        start = 0
        for start in range(len(a)):
            if chk.join(b).replace(' ' * size, '') in a[start:start+len(chk.join(b) + " " * size):1+size]:
                answer += 1
        size += 1
    return answer

print(solution('bbbabcbdacbbbd', 'bbb'))