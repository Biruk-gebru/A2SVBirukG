# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
s = 0

for x in range(1, n + 1):
    sol = set()
    d = 2
    while d * d <= x:
        while x % d == 0:
            sol.add(d)
            x //= d
        d += 1
    if x > 1:
        sol.add(x)
    if len(sol) == 2:
        s += 1
print(s)