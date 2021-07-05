def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for x, y in zip(participant, completion):
        if x != y:
            return x # 중복된 값일 경우 
    return participant[-1] # 맨 마지막 사람 출력