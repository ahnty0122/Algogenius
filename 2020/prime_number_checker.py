num=int(input())

flag=True

for i in range(2,num,1):
    if num%i==0:
        flag=False

if flag:
    print("소수")
else:
    print("소수 아님")