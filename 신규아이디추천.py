# 정규표현식 사용
import re
def solution(new_id):
    answer = ''
    # 소문자로 치환
    new_id = new_id.lower()
    # 알파벳 소문자, -, ., _, 숫자 빼고 제거
    new_id = re.sub(r'[^a-z\-\.\_\d]','', new_id)
    # .이 2개 이상 반복되면 제거
    new_id = re.sub(r'\.\.+', '.', new_id)
    # 시작문자가 .이면 제거
    new_id = re.sub(r'^\.', '', new_id)
    # 끝문자가 .이면 제거
    new_id = re.sub(r'\.$', '', new_id)
    # 아무것도 없으면 a 대입
    if len(new_id) == 0:
        new_id = re.sub(r'', 'a', new_id)
    # 길이가 16이상이면 15개로 자르기 + 끝 문자가 .이면 제거
    new_id = re.sub('\.$', '', new_id[0:15])
    # 길이가 2 이하이면 3이 될 때까지 마지막 문자 추가
    while len(new_id) < 3:
        new_id += new_id[-1:]
    answer = new_id
    return answer

# 정규표현식 다른 풀이
import re
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

# 정규표현식 사용 X 풀이
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer