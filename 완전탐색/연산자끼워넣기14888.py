import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

# 연산자의 개수만큼 탐색
# 연산자 존재하면 그 연산을 수행하며 재귀 호출 통해 탐색

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + a[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - a[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * a[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / a[depth]), plus, minus, multiply, divide - 1)


dfs(1, a[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)