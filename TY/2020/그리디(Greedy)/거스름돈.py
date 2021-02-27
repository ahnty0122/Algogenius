n = int(input()) # 거스름돈

count = 0

list = [500,100,50,10] # 화폐단위

for coin in list:
	count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 
	n %= coin

print(count)
