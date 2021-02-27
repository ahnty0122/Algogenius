'''
scores = list( map (int , input().split(" ") ) )
max_val=-1
max_count=0
for i in scores : # 반복문 (N)
    count=0
    for j in scores : # 반복문 (N)
        if i==j:
            count+=1 # (N제곱)
    if max_count < count:
        max_count=count
        max_val=i

print(max_count)
print(max_val)
'''


# 0~100 까지 점수가 들어온다 (정수)
# 가장 자주 등장하는 점수 출력

import sys
user_input=map(int,sys.stdin.readline().split(' '))
scores=[0 for i in range(101)] 
for i in user_input: #(N)
	scores[i]+=1
print(scores.index(max(scores)))
