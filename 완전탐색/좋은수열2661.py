n = int(input())

# 인접한 두 부분 수열 중 가장 긴 경우는 현재 수열 길이의 1/2
# len(num) // 2까지 인접한 두 수열이 일치하는지 파악하기
def check(num):
    for idx in range(1, len(num) // 2 + 1):
        if num[-idx:] == num[-(idx * 2) : -idx]:
            return False
    return True

# 1,2,3 순서대로 수열에 덧붙여 진행
# 종료 조건은 수열의 길이가 n일 때 + 가능한 수열 중 최소 찾아야 하니깐 exit()
def recursive(num):
    if len(num) == n:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

recursive('1')