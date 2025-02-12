# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

t = int(input())
x = []
y = []
z = []
for _ in range(t):
    num = list(map(int, input().split()))
    x.append(num[0])
    y.append(num[1])
    z.append(num[2])
xSum = sum(x)
ySum = sum(y)
zSum = sum(z)
if xSum!= 0 or ySum != 0 or zSum != 0:
    print("NO")
else:
    print("YES")
