# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sol = 0
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            sol += 1
            i += 1
        i += 1
    print(sol)
        