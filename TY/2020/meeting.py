n = int(input())
begin = [0 for i in range(101)]
end = [0 for i in range(101)]
for i in range(n):
	begin[i], end[i] = list(map(int, input().strip().split(' ')))

order = [(end[i],begin[i]) for i in range(n)]
order.sort()

def schedule():
	earliest = 0
	selected = 0
	begin = 0
	for i in range(n):
		mbegin = order[i][1]
		mend = order[i][0]
		
		if earliest<=mbegin:
			earliest = mend
			selected += 1
	return selected

print(schedule())