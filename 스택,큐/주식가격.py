# 이중 for문
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i,len(prices)-1):
            if prices[i] <= prices[j]:
                answer[i] += 1 
            else:
                break

    return answer

# 큐 이용
from collections import deque
def solution1(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

print(solution1([1, 2, 3, 2, 3]))