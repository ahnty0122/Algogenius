# 1 1 2 3 5 8 13 21 ...
# fib(n) = fib(n-1) + fib(n-2)

# 재귀 함수를 이용한 방법 
# 기저 사건 : 가장 최종적으로 도착하는 조건

def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))




'''
fib=[0 for i in range(31)]

n=30

fib[1]=1
fib[2]=1

for i in range(3,n+1):
    fib[i]=fib[i-1]+fib[i-2]

print(fib[8])

'''

'''
def fib(n):
    if n==2:
        return 1
    if n==1:
        return 1
    
    return fib(n-1)+fib(n-2)

print(fib(7))
'''

