import sys 
input = sys.stdin.readline

n = map(int, input()) 
a = list(map(int, input().split())) 

pool = {} 
for k in a: 
    pool[k] = 1 

print(pool)

m = map(int, input()) 
b = list(map(int, input().split())) 
for t in b: 
    if t in pool:
        print(1) 
    else: 
        print(0)