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
L, C = map(int, input().split())
alpha = list(map(str, input().split()))
out = []
all_out = []
alpha.sort()

def solve(depth, idx, L, C):
    if depth == L:
        all_out.append(''.join(map(str, out)))
        return
    for i in range(idx, C):
        out.append(alpha[i])
        solve(depth+1, i+1, L, C)
        out.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

solve(0, 0, L, C)
password(all_out)