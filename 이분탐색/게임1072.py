import sys
input = sys.stdin.readline
x, y = map(int, input().split())

z = int(100 * y / x)

if z >= 99:
    print(-1)
else:
    ans = 0
    start = 0
    end = 1000000000
    while(start <= end):
        mid = (start + end) // 2
        if int(100 * (y + mid) / (x + mid)) <= z:
            start = mid + 1
        else:
            end = mid - 1
    print(end + 1)