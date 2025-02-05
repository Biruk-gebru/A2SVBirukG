# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

import sys
from collections import Counter
input = sys.stdin.readline

t=1
t= int(input())
for _ in range(t):
	s = list(input())
	s.pop()
	t = list(input())
	t.pop()
	p = list(input())
	p.pop()
	k = s + p
	dict_s = Counter(s)
	dict_t = Counter(t)
	dict_k = Counter(k)
	flag = True
	for elem in s: 
		if elem in t:
			if dict_s[elem]> dict_t[elem]:
				flag = False
		else:
			flag = False
				
	for elem in t:
		if elem in k:
			if dict_k[elem] < dict_t[elem]:
				flag = False
		else:
			flag = False
	i = 0 
	for elem in t:
		if elem == s[i]:
			i+=1
			if i >=len(s):
				break

	if i < len(s):
		flag = False
		
	if flag:
		print("YES")
	else:
		print("NO")