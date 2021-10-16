# 백트래킹

# dfs 이용한 풀이
# 해당 원소를 포함하는 경우와 포함하지 않는 경우로 나누어 가지가 뻗어나가는 형태
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))

def dfs(v, sum):
    global cnt
    if v >= n:
        return
    sum += a[v]
    if sum == s:
        cnt += 1
    dfs(v + 1, sum - a[v])
    dfs(v + 1, sum)

cnt = 0
dfs(0, 0)
print(cnt)

# 조합을 이용한 풀이
# import sys
# input = sys.stdin.readline
# from itertools import combinations

# n, s = map(int, input().split())
# a = list(map(int, input().split()))

# count = 0

# for i in range(1, n + 1):
#     per = combinations(a, i)
#     for j in list(per):
#         if sum(j) == s:
#             count += 1
# print(count)