def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    
    # 다리를 지나는 동안
    while q:
        # 시간 1초 증가
        time += 1
        q.pop(0)
        # pop(0)으로 첫 번째 원소부터 꺼내기
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight: # weight가 기준점 이하이면
                q.append(truck_weights.pop(0)) # 트럭 하나 더 추가
            else:
                q.append(0)
    return time

# bridge_length 2
# weight 10
# truck_weights [7,4,5,6]
# return 8