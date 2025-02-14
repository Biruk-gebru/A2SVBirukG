# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
 
n , k = map(int, input().split())
arr = list(map(int, input().split()))
 
ss = defaultdict(int)
left = 0
sol = 0
l = 0
for right in range(n):
    ss[arr[right]] += 1
    while len(ss) > k:
        ss[arr[left]] -= 1
        if ss[arr[left]] == 0:
            del ss[arr[left]]
        left += 1
    if sol < right - left + 1:
        sol = right - left + 1
        l = left
 
print(l+1, l + sol)