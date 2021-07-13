def solution(genres, plays):
    answer = []
    dict_music = {}
    dict_rank = {}
    for i in range(len(genres)):
        if genres[i] in dict_music:
            dict_music[genres[i]].append((plays[i], i))
            dict_rank[genres[i]] += plays[i]
        else:
            dict_music[genres[i]] = [(plays[i], i)]
            dict_rank[genres[i]] = plays[i]
    dict_rank = sorted(dict_rank.items(), key=lambda x: x[1], reverse=True)
    for key in dict_rank:
        chk = 0
        dict_music[key[0]] = sorted(dict_music[key[0]], key = lambda x : (-x[0], x[1]))
        for i in dict_music[key[0]]:
            answer.append(i[1])
            chk += 1
            if chk == 2:
                break
    print(dict_rank)
    print(dict_music)
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# input
# genres = ["classic", "pop", "classic", "classic", "pop"]    
# plays = [500, 600, 150, 800, 2500]

# output 장르별로 들은 횟수 높은 순서대로 2개 index 출력 
# [4, 1, 3, 0]

# dict_music --> index와 함께 튜플로 사전 value 담기
# dict_rank --> 플레이 횟수 합한 값 넣기
# sorted, lambda로 딕셔너리 정렬
# dict_music[key[0]] = sorted(dict_music[key[0]], key = lambda x : (-x[0], x[1]))
# 첫번째 인자로 내림차순 정렬 먼저, 두번째 인자로 오름차순 정렬