# 해시
import collections
def solution(participant, completion):
	answer = collections.Counter(participant) - collections.Counter(completion)
	return list(answer.keys())[0]

# ["leo", "kiki", "eden"]	["eden", "kiki"]
# leo

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))