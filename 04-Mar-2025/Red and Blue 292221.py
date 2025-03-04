# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1,n):
        a[i] = a[i-1] + a[i]
    m = int(input())
    b = list(map(int, input().split()))
    for i in range(1,m):
        b[i] = b[i-1] + b[i]
    print(max(0, max(a), max(b), max(a) + max(b)))
    