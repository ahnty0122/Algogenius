import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()


result = []

for i in b:
    start = 0
    end = n - 1
    flag = 0
    while(start <= end):
        mid = (start + end) // 2
        if i < a[mid]:
            end = mid - 1
        elif i > a[mid]:
            start = mid + 1
        elif i == a[mid]:
            flag = 1
            break
    result.append(flag)

for i in result:
    print(i)