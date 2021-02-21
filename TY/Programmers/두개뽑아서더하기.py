def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
    answer.sort()
    return answer


#### 다른 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
1. set 자료형 이용, 중복된 list 넣으면 set은 중복된 값은 하나만 포함해 정의함
2. sorted(list), list.sort() 내장함수
'''