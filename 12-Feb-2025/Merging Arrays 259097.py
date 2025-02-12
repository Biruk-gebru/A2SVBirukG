# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

m, n = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
i, j = 0, 0
sol = []

while i < m or j < n:
    if j == n or i < m and l1[i] < l2[j] :
        sol.append(l1[i])
        i += 1
    else:
        sol.append(l2[j])
        j += 1

print(*sol,sep=' ')