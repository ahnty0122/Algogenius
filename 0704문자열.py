from itertools import permutations
def solution(S, pattern):
    list_p = permutations(list(pattern), len(list(pattern)))
    cnt = 0
    for i in set(list_p):
        for j in range(len(S)):
            if ''.join(i) == S[j:j+ len(list(pattern))]:
                cnt += 1
    return cnt