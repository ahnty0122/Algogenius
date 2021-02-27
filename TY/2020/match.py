import sys

def solution(china, korea):
	china.sort()
	korea.sort()
	win = 0
	for ch in china:
		for i, ko in enumerate(korea):
			if ch <= ko:
				win += 1
				korea.pop(1)
				break
	return win

china = list(map(int, sys.stdin.readline().split()))
korea = list(map(int, sys.stdin.readline().split()))
print(solution(china, korea))