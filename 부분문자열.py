def solution(a, b):
    answer = 0
    size = 0
    while(len(b) + size * (len(b) - 1) <= len(a)):
        chk = ' ' * size
        start = 0
        for start in range(len(a)):
            if chk.join(b).replace(' ' * size, '') in a[start:start+len(b) + size * (len(b) - 1):1+size]:
                print(chk.join(b), a[start:start+len(b) + size * (len(b) - 1) + 1])
                answer += 1
        size += 1
    return answer

print(solution('bbbabcbdacbbbd', 'bbb'))