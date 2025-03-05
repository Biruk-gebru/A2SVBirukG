# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n , k = map(int, input().split())

a = list(map(int, input().split()))

diff = []
for i in range(n-1):
    diff.append(a[i+1] - a[i])

nu = len(diff) - k + 1
diff.sort()
print(sum(diff[:nu]))

