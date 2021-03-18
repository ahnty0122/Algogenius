n=int(input()) #햄버거 개수
e=list(map(int,input().strip().split(' '))) #먹는데 걸리는 시간
h=list(map(int,input().strip().split(' '))) #데우는데 걸리는 시간

l=[(e[i],h[i]) for i in range(n)]
#print(l)

l= sorted(l,reverse=True) #sorted
#print(l)

beginEat=0
tmp=0

for i in l:
	beginEat+=i[1]
	tmp=max(tmp,beginEat+i[0])

print(tmp)

# 입력으로 햄버거 개수, 먹는데 걸리는 시간, 데우는데 걸리는 시간
# 전자레인지는 하나밖에 없고, 한명씩 데우고 끝나면 데워야함
# 출력으로 먹는데 걸리는 최소 시간 출력