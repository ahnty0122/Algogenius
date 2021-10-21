def solution(array, commands):
    answer = []
    for i in commands:
        test = array[i[0] - 1:i[1]]
        test.sort()
        answer.append(test[i[2] - 1])
    return answer