# def fence(h)  h : 높이 들어있는 리스트
    #반복문 1 : left
        #반복문 2 : right
            #높이 left ~ right 에서 최소값 찾기
            #넓이 중 최대값 찾기 
    #최대값

# 울타리 자르기

def fence(h):
    tmp=0
    n=len(h)

    for left in range(0,n,1):
        minH=h[left]
        for right in range(0,n,1):
            minH=min(minH,h[right])
            tmp=max(tmp,(right-left+1)*minH)
    
    return tmp