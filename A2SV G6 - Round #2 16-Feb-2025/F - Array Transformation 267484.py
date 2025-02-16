# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter  

t = int(input())  

for _ in range(t):  
    n = int(input())  
    vals = sorted(Counter(list(map(int, input().strip().split()))).values())
    
    min_removals = float('inf')
    prev_sum = 0
    total_sum = sum(vals)
    for i, count in enumerate(vals):
        removed = prev_sum + total_sum - count * (len(vals) - i)
        total_sum -= count
        prev_sum += count

        min_removals = min(min_removals, removed)  

    print(min_removals)