# KMP 문자열 검색 알고리즘
def make_pi():
    pi = [0 for i in range(0, len(P))]

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]: # 같지 않을 때
            j = pi[j - 1] # 이전의 맞은 부분으로 돌아가서 다시 비교

        if P[i] == P[j]: # 같을 때
            j += 1 # j 증가시키고 테이블 갱신
            pi[i] = j
    return pi


def solution(pi):
    result = []
    count = 0

    j = 0
    for i in range(0, len(T)):

        while j > 0 and T[i] != P[j]: # 같지 않을 때
            j = pi[j - 1] # 이전의 맞은 부분까지 돌아가서 다시 비교

        if T[i] == P[j]: # 같으면
            if j == (len(P) - 1): 
                result.append(i - len(P) + 2) # 위치추가
                count += 1 # 개수추가
                j = pi[j] # 위치 옮겨주고 다시 탐색
            else:
                j += 1 # j 늘려주기

    print(count)
    for element in result:
        print(element)


T = input()
P = input()
solution(make_pi())