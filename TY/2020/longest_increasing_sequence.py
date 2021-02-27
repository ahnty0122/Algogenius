# 최대 증가 부분 수열
# 수열에서 0개 이상의 숫자를 지우고 남은 수열 중 -> 부분 수열 
# 숫자들이 순수하게 증가만 하는 수열을 증가 부분 수열이라고 한다.
# 이들 중 가장 긴 수열을 최대 증가 부분 수열이라고 부른다.
# 최대 증가 부분 수열의 길이 출력
'''
n=int(input())
s=list(map(int,input().strip().split(" ")))

def lis(nums): #nums 리스트
	if len(nums) == 0: #빈 리스트가 왔을 때 -> 다 본것 
		return 0
	tmp=0
	for i in range(len(nums)): 
		cropped=[] 
		for j in range(i+1,len(nums)):
			if nums[i]<nums[j]:
				cropped.append(nums[j])
		tmp=max(tmp,1+lis(cropped))
	return tmp
print(lis(s))
'''
cache=[-1 for i in range(100)]
n=int(input())
s=list(map(int,input().strip().split(" ")))
def lis(start):
	tmp=cache[start+1]
	if tmp!=-1:
		return tmp
	tmp=1
	for i in range(start+1,n,1):
		if start ==-1 or s[start]<s[i]:
			tmp = max(tmp,lis(i)+1)
	return tmp

print(lis(0))


'''
nums = [3, 2, 1, 7, 5, 4, 6]
i=3             
c=[7,5,4,6]   	nums=[7,5,4,6] 
              	i=7
			  	c=[]
				1+0
				  			nums=[] return 0
				tmp=1
				i=5
				c=[6]
				1+1
							nums=[6]
							i=6
							c=[]
							1+
										nums=[] return 0
'''