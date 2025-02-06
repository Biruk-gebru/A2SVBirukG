# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import math
from collections import defaultdict
t  = int(input())

for _ in range(t):
    l = int(input())
    nums = list(map(int,input().split()))

    counter = defaultdict(int)
    for n in nums:
        i = 2
        while i * i <= n:
            while n % i == 0:
                counter[i] += 1
                n //= i
            i += 1
        if n > 1:
            counter[n] += 1
    
    if any(v for v in counter.values() if v % l != 0):
        print("NO")
    else:
        print("YES")


