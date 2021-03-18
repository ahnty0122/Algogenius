from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순
print(queue) # 나중에 들어온 원소부터 출력

# 3, 7, 1, 4
# 4, 1, 7, 3