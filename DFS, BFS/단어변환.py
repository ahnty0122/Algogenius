from collections import deque

def can_change(cur_word, words): 
    cand = []
    for word in words:
        diff = [True for x, y in zip(cur_word, word) if x != y] # 한 글자만 다른 단어 체크 위해 배열 생성
        if len(diff) == 1:
            cand.append(word)
    return cand

def solution(begin, target, words):
    visited = set([begin]) # 방문확인
    que = deque([(begin, 0)]) # 횟수까지 체크
    while que:
        cur_word, cur_count = que.popleft() # 현재 단어, 카운트
        if cur_word == target:
            return cur_count
        for word in can_change(cur_word, words): # cur_word 기준으로 words 중 바꿀 수 있는 단어 체크
            if word not in visited: 
                que.append((word, cur_count + 1)) # 그 중 방문하지 않은 word 추가 + 횟수도
                visited.add(word) # 그 중 방문하지 않은 word 추가
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))