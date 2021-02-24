# 해쉬 구현
def solution(phone_book):
    answer = True
    hash_map = {}
    
    for i in phone_book:
        hash_map[i] = 1
    
    for i in phone_book:
        chk = ""
        for j in i:
            chk += j
            if chk in hash_map and chk != i:
                answer = False        
    return answer

# collections 이용한 해쉬 구현
import collections
def solution(phone_book):
    answer = True
    hash_book = collections.Counter(phone_book)
    for i in phone_book:
        chk = ""
        for j in i:
            chk += j
            if chk in hash_book and chk != i:
                answer = False
    return answer

# 같은 아이디어로 해쉬 사용하지 않고 list를 사용해 봤으나 효율성에서 문제
# list는 선형 탐색 O(N), 해쉬는 딕셔너리 자료형으로 O(1)
def solution(phone_book):
    answer = True
    for i in phone_book:
        chk = ""
        for j in i:
            chk += j
            if chk in phone_book and chk != i:
                answer = False
    return answer

# zip으로 phonebook, phoneBook[1:] 묶어서 앞뒤값 비교
# 겹치지 않는 p2가 p1으로 시작하는지 확인
def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(zip(phoneBook, phoneBook[1:]))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True