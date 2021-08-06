# def dfs(nums, i, n, t):
#     ret = 0
#     if i==len(nums):
#         if n==t: return 1
#         else: return 0
#     ret += dfs(nums, i+1, n+nums[i], t)
#     ret += dfs(nums, i+1, n-nums[i], t)
#     return ret

# def solution(numbers, target):
#     answer = dfs(numbers, 0, 0, target)
#     return answer

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])  
    queue.append([-1*numbers[0],0]) # 인덱스를 같이 저장
    while queue:
        temp, idx = queue.popleft() 
        print(idx)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1    
    return answer

print(solution([1, 1, 1, 1, 1], 3))