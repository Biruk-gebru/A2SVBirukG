# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
 
    flag = True
    su = 0
    ma = float('-inf')
    for i in range(n):
        if flag:
            if arr[i] < 0:
                flag = False
                if ma > float('-inf'):
                    su += ma
                ma = float('-inf')
                         
        else:
            if arr[i] > 0:
                flag = True
                if ma > float('-inf'):
                    su += ma
                ma = float('-inf')
        ma = max(ma,arr[i])
    if ma > float('-inf'):
        su += ma
    print(su)