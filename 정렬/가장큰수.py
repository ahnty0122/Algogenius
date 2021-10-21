def solution(numbers):
    numbers = list(map(str, numbers)) # str로 형 변환 후 배열 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True) 
    # 문자열은 ASCII 코드로 치환되어 정렬
    # 세 자리 수로 변환한 뒤 비교하기 위해 * 3 해서 정렬해주기
    return str(int(''.join(numbers)))

# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"