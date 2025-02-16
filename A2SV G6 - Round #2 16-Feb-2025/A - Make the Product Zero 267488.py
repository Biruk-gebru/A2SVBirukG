# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

t=1
#t= int(input())
for _ in range(t):
	len = int(input())
	nums = list(map(int, input().split()))
	minA = float('inf')
	
	for elem in nums:
		if abs(elem) < minA:
			minA = abs(elem)
	print(abs(minA))