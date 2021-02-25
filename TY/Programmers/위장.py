import collections
def solution(clothes):
    answer = 1
    hash_cloth = collections.Counter([i[1] for i in clothes])
    for i in hash_cloth:
        answer *= (hash_cloth[i]+1)
    return answer - 1



########### 다른 풀이
# 2차원 리스트 해시로 만들기
def solution(clothes):
    answer = 1
    
    d = {}
    for val, key in clothes:
        # key가 같으면 val 추가
        if key in d.keys():
            d[key].append(val)
        # key에 val 할당
        else:
            d[key] = [val]
    
    for val in d.values():
        # 조합 계산하기 위해 +1 해준 값 곱하기
        answer *= (len(val)+1)
    
    # 마지막에 아무것도 착용하지 않은 경우의 수 빼주기
    return answer - 1

# collections.Counter() 이용
from collections import Counter

def solution(clothes):
    answer = 1
    # 이차원리스트 clothes에서 clothes[:][0]은 value
    # cloth[1] 형태 --> ['yellow_hat', 'headgear'][1]
    kind = Counter([cloth[1] for cloth in clothes])
    # {'headgear': 2, 'eyewear': 1}

    for i in kind:
           answer *= (kind[i] + 1)
           
    answer -= 1
    
    return answer