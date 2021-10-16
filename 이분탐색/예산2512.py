import sys
input = sys.stdin.readline

n = int(input())
bud = list(map(int, input().split()))
m = int(input())

start = 1
end = max(bud)

while(start <= end):
    count = 0
    mid = (start + end) // 2
    for i in bud:
        if i <= mid:
            count += i
        else:
            count += mid
    if count <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)