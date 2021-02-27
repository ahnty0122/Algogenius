inputlimit = int(input())
inputcount = 0
eflag = False
queue = []
estr = 'eE'

while True:
	num = input()
	if num == 'e' or num == 'E':
		if len(queue) == 10:
			inputcount += 1
			eflag = True
	elif num == 'd' or num == 'D':
		inputcount += 1
		queue.remove(0)
		if inputcount == inputlimit:
			break
	elif eflag:
		queue.append(int(num))
		eflag = False
		if inputcount == inputlimit:
			break
	else:
		break

for i in queue:
	print(i, end = " ")