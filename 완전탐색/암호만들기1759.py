# 백트래킹

# combinations 사용
# import sys
# from itertools import combinations

# vowels = ['a', 'e', 'i', 'o', 'u']
# L, C = map(int, sys.stdin.readline().split())
# pwd = sorted(list(map(str, sys.stdin.readline().split())))

# comb = combinations(pwd, L)

# for c in comb:
#     print(c)
#     count = 0
#     for letter in c:
#         if letter in vowels:
#             count += 1

#     if (count >= 1) and (count <= L - 2):
#         print(''.join(c))


# 백트래킹 정의 풀이
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
s = list(map(str, input().split()))
s.sort()

pre = []
result = []
def dfs(depth, idx):
    if depth == l:
        result.append("".join(pre))
        return
    for i in range(idx, c):
        pre.append(s[i])
        dfs(depth + 1, i + 1)
        pre.pop()

dfs(0, 0)

for i in result:
    count_vo = 0
    for j in i:
        if j in 'aeiou': count_vo += 1
    if count_vo >= 1 and count_vo <= (l - 2):
        print(i)