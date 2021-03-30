def solution(numbers, target):
    answer = 0
    current_list = [numbers[0], -numbers[0]]
    print(current_list)
    for i in range(1, len(numbers)):
        next_number = numbers[i]
        print(next_number)
        next_list = []
        for num in current_list:
            next_list.append(num + next_number)
            next_list.append(num - next_number)

        current_list = next_list
        print(current_list)
    for num in current_list:
        if num == target:
            answer += 1
    return answer

from collections import deque

def solution1(numbers, target):
    answer = 0
    queue = deque([(0, 0)]) # sum, level
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))
    return answer

print(solution1([1, 1, 1, 1, 1], 3))