n = int(input())

init = 1 
cnt = 1
while n > init :
    init += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복횟수
print(cnt)