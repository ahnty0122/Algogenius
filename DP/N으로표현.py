# 모든 N에 대한 결과 저장해놓기
# i 횟수만큼 연산..
def solution(N, number):
    possible_set = [0,[N]] # 연산 조합으로 나올 수 있는 가능한 숫자들
    if N == number: 
        return 1
    for i in range(2, 9):  
        case_set = [] # 임시로 사용할 셋, i 별로 셋 만들어 possible set에 추가
        basic_num = int(str(N) * i) # 같은 숫자 반복되는 거 추가. 5, 55, 555 이런거
        case_set.append(basic_num)
        for i_half in range(1, i // 2 + 1): # 사용되는 숫자의 횟수 구할 때 절반 이상으로 넘어가면 같은 결과만 나오니깐 절반까지만 사용 
            for x in possible_set[i_half]:
                for y in possible_set[i - i_half]: # x와 y를 더하면 i 가 되도록 만든 수다. 
                    case_set.append(x + y) # 각 사칙연산 결과를 더한다.
                    case_set.append(x - y)
                    case_set.append(y - x)
                    case_set.append(x * y)
                    if y != 0:
                        case_set.append(x / y)
                    if x != 0:
                        case_set.append(y / x)
            if number in case_set:
                return i
            possible_set.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1 #N 이 8까지 답이 없으면 -1을 출력

print(solution(5, 12))