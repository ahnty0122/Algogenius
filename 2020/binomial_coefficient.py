#Memoization 통해 이항 계수 계산하는 프로그램


# n 개중에 r 개를 뽑는 경우의 수 -> r=0 , n==r
'''
def com(n,r):
    # 기저 사건
    if n==r:
        return 1
    if r==0:
        return 1

    return com(n-1,r-1) + com(n-1,r)

print(com(6,2))
'''


#binomial coefficient
'''
def bino(n,r):
    if r==0 or n==r:
        return 1
    return bino(n-1,r-1)+bino(n-1,r)
'''


#기저 사건, cache 사용
cache=[[-1 for i in range(31)] for j in range(31)]

def bino(n,r):
    if r==0 or r==n :
        return 1
    if cache[n][r] != -1:
        return cache[n][r]
    cache[n][r] = bino(n-1,r-1) + bino(n-1,r)
    return cache[n][r]

print(bino(5,2))
