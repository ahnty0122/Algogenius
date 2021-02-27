p = list(map(int, input().split()))
i = list(map(int, input().split()))

def printPostOrder(preorder, inorder):
		n = len(preorder)
		if n==0: # 재귀함수, 기저 사건 - 서브 트리를 전부 순회 했을 때
			return
		root = preorder[0]
		L = inorder.index(root)
		
		printPostOrder(preorder[1:L+1], inorder[0:L]) # 왼쪽 서브트리
		printPostOrder(preorder[L+1:n], inorder[L+1:n]) # 오른쪽 서브트리
		print(root, end = " ")
		
printPostOrder(p, i)