# 괄호가 옳은 괄호면 True
# 잘못됐으면 False를 출력한다.

# 괄호의 문법
# 1. 나중에 열린 괄호가 먼저 닫혀야 한다. (Last in First out - LIFO)
# 2. 괄호는 3종류가 있고 종류별로 매칭되야 한다. 교차할 수 없다.
# 3. 열린 괄호는 닫혀야 한다 (스택이 비어있다 )

# 열린 괄호가 들어오면 -> 스택에 push (1)
# 닫힌 괄호가 들어오면 -> 스택의 최상단(top) -> 짝이 맞는지 비교 -> 짝이 맞으면 stack pop (2)
# 모든 문자열을 순회한 후 스택이 비어있는지 확인한다. (3)

def wellMatched(s):
    opening=["[","{","("]
    closing=["]","}",")"]
    stack=[]

    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            if i!=closing[opening.index(stack[-1])]:
                return False
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False

s=input()
print(wellMatched(s))
