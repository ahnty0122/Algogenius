# 랜선의 길이 구하기
# 랜선의 길이 움직여 랜선 개수 채우는지 보기

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start = 1
end = max(lan)

while(start <= end):
    mid = (start + end) // 2
    count = 0
    for i in lan:
        count += (i // mid)
    if count >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)