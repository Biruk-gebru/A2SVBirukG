# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import defaultdict
t = int(input())

for _ in range(t):
    n,k,d = map(int, input().split())
    a = list(map(int, input().split()))
    holder = defaultdict(int)
    for i in range(d):
        holder[a[i]] += 1
    sol = len(holder)
    left = 0
    for right in range(d,n):
        holder[a[left]] -= 1
        if not holder[a[left]]:
            del holder[a[left]]
        holder[a[right]] += 1
        left += 1
        sol = min(sol,len(holder))
    print(sol)
