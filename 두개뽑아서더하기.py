def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
    answer.sort()
    return answer


#### �ٸ� Ǯ��
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
1. set �ڷ��� �̿�, �ߺ��� list ������ set�� �ߺ��� ���� �ϳ��� ������ ������
2. sorted(list), list.sort() �����Լ�
'''