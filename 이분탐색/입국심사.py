def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n # 가장 비효율적인 심사 시간
    while left <= right:
        mid = (left+ right) // 2
        count = 0
        for i in times:
            count += mid // i
            # 모든 심사관 안거치고 mid분 동안 n명 이상의 심사를 할 수 있다면 break
            if count >= n:
                break
        if count >= n:
            right = mid - 1
        elif count < n:
            left = mid + 1
    return left

print(solution(6, [7, 10]))